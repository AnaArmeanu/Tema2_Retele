from scapy.all import *

eth = Ether(dst = "ff:ff:ff:ff:ff:ff")
arp = ARP(pdst = "198.13.13.0/16")
ans, unans = srp(eth / arp)
print "IP -- MAC"
for answer in ans:
    print answer[1].psrc + " -- " + answer[1].hwsrc
