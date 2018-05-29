#TCP handshake
from scapy.all import *
from struct import *
import sys

#setare header IP
ip = IP()
ip.src = '198.13.0.15' # sursa :  md1
ip.dst = '198.13.0.14' # destinatia : rt1
ip.tos = int('011110' + '11', 2) #setare DSCP pe valoarea AF33(DSCP Value = 011110) pt vide streaming si ECN cu notif de congestie
#DSCP && ECN

#setare header TCP
tcp = TCP()
tcp.sport = 80 # port la alegere
tcp.dport = 10000 # portul destinatie pe care ruleaza serverul

op_index = TCPOptions[1]['MSS']
op_format = TCPOptions[0][op_index]
val = struct.pack(op_format[1],2) # val e acum o pereche de tip (optiune/format , valoare)
tcp.options = [('MSS',val)] # setare [MSS,2]

tcp.seq = 100 # un sequence number la alegere
tcp.flags = 'S' #setare flag SYN, I want to SYN (cerere de comunicare)
raspuns_syn_ack = sr1(ip/tcp) #SYN,ACK - I got it ACK, want to SYN also (acord la comunicare + cerere comunicare inapoi)
tcp.seq += 1
tcp.ack = raspuns_syn_ack.seq + 1
tcp.flags = 'A' #setare flag ACK - Acknoledgement - Good, connection established
ACK = ip / tcp
send(ACK)

for ch in "abc":
    tcp.flags = 'PAEC'#setare flaguri PSH ACK ECE CWR
    tcp.ack = raspuns_syn_ack.seq + 1
    print "Am trimis: " + ch
    rcv = sr1(ip/tcp/ch)
    tcp.seq += 1

tcp.flags = 'R'
RES = ip/tcp
send(RES)