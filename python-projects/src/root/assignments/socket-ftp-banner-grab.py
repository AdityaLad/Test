'''
Created on Sep 8, 2014

@author: lada
'''
import socket

def retrieveBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def main():
    get = retrieveBanner("ftp.microsoft.com", 21)
    print get
    
if __name__ == '__main__':
    main()

