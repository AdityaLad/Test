'''
Created on Sep 8, 2014

@author: lada
'''
import os
import sys
import socket

def usage_check():
    if len(sys.argv) != 3:
        print "Usage: %s <filename> <port>" % sys.argv[0]
        exit(1)

    if not os.access(sys.argv[1], os.F_OK):
        print "Cannot access your file"

def read_file(filename):
    f = open(filename, 'r')    
    for line in f.readlines():
        print line
        return line
        
def main():
    socket.setdefaulttimeout(2)
    try:
        s = socket.socket()
        ipaddress = read_file(sys.argv[1])
        s.connect((ipaddress, int(sys.argv[2])))
        response = s.recv(1024)
        print response
        if bool(response):
           print "Connection successful"
    except:
        print ipaddress, "at port", str(sys.argv[2]), "is not open"

if __name__ == '__main__':
    main()
        
    