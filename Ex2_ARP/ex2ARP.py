
from scapy.all import *
 
eth = Ether(dst = "ff:ff:ff:ff:ff:ff")
#arp = ARP(pdst = '198.13.13.1')#pdst = ip destinatie
arp = ARP(pdst = "198.13.13.0/16")
#subnetul lui net
answered,unanswered = srp(eth / arp, timeout = 2, inter = 0.1 )
#srp trimite pachete in retea si primeste raspunsuri (protocoale pentru pachete: Ethernet si ARP)
#inter = timp de asteptare intre pachete - 0.1 secunde
#timeout = timp asteptare confirmare
print "IP -- MAC\n"
for snd,rcv in answered:
    print rcv[ARP].psrc + " -- " + rcv[Ether].src

    
