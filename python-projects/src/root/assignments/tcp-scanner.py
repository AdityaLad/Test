'''
Created on Sep 8, 2014

@author: lada
'''
import os
import sys
import socket

def usage_check():
    if len(sys.argv) != 3:
        print "Usage: %s <ip> <port1>,<port2>.." % sys.argv[0]
        exit(1)

def scanme(ipaddress, port):
    socket.setdefaulttimeout(2)
    
    try:
        s = socket.socket()
        s.connect((ipaddress, int(port)))
        banner = s.recv(1024)
        print "[+] %d/tcp - open - %s" % (int(port),banner)
        s.close()
    except:
        print "[-] %d/tcp - open" % int(port)

       
def main():
    usage_check()
    for ports in sys.argv[2].split(','):
        scanme(sys.argv[1],ports)
    

if __name__ == '__main__':
    main()
        
    