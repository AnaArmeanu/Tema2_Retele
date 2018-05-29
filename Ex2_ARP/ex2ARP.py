
from scapy.all import *
 
eth = Ether(dst = "ff:ff:ff:ff:ff:ff")
arp = ARP(pdst = "198.13.13.0/16")#subnet net
ans, unans = srp(eth / arp)
#srp trimite pachete in retea si primeste raspunsuri (protocoale pentru pachete: Ethernet si ARP)
print "IP -- MAC\n"
for snd,rcv in ans:
    print rcv[ARP].psrc + " -- " + rcv[Ether].src

    
