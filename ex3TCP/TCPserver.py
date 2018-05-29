# TCP Server
import socket
import logging
import time
import sys

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 10000

adresa = '0.0.0.0'
server_address = (adresa, port)
sock.bind(server_address)
logging.info("Serverul a pornit pe adresa %s si portul portul %d", adresa, port)
sock.listen(1) # asteptam acea singura conexiune
logging.info('Asteptam conexiune (una singura)...')
conexiune, address = sock.accept()
logging.info("Handshake cu %s", address)
while True:
    data = conexiune.recv(1) # doar 1 byte = ce a primit
    logging.info('Content primit : "%s"', data)
    data = str(data).upper()
    logging.info('Trimis : "%s"', data)
    conexiune.send(data)#trimit inapoi mesaj de un byte, "preferabil o litera"
conexiune.close()
sock.close()