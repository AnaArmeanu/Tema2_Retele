#varianta stop-and-wait
def window(iterable, size=2):
    i = iter(iterable)
    win = []
    for e in range(0, size):
        win.append(next(i))
    yield win
    for e in i:
        win = win[1:] + [e]
        yield win

# UDP client
import socket
import logging
import sys
import array

secv = []
for idx in range(0, 10):
    secv.append(idx)
logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 10000
adresa = 'localhost'
server_address = (adresa, port)
mesaj = sys.argv[0]

try:
    secv = []
    for idx in range(1, 1001):
        secv.append(idx)
    for i in secv:
        logging.info('Trimitem mesajul "%s" catre %s', i, adresa)
        sent = sock.sendto(str(i).strip('[]'), server_address)
        logging.info('Asteptam un raspuns...')
        data, server = sock.recvfrom(4096)
        logging.info('Content primit: "%s"', data)

finally:
    logging.info('closing socket')
    sock.close()
    
def slidingWindow(sequence,winSize,step=1):
        #=> generator care itereaza prin bucatile de input 
     
        # Verify the inputs
        try: it = iter(sequence)
        except TypeError:
            raise Exception("**ERROR** sequence must be iterable.")
        if not ((type(winSize) == type(0)) and (type(step) == type(0))):
            raise Exception("**ERROR** type(winSize) and type(step) must be int.")
        if step > winSize:
            raise Exception("**ERROR** step must not be larger than winSize.")
        if winSize > len(sequence):
            raise Exception("**ERROR** winSize must not be larger than sequence length.")
     
        # Pre-compute number of chunks to emit
        numOfChunks = ((len(sequence)-winSize)/step)+1
     
        # Do the work
        for i in range(0,numOfChunks*step,step):
            yield sequence[i:i+winSize]
