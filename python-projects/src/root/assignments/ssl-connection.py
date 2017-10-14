'''
Created on Sep 11, 2014

@author: lada
'''
import socket
import ssl

host="www.google.com"
port=443
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv3, ciphers="HIGH")

server_certificate = s.getpeercert()

print s.proto, s.ssl_version, s.getpeercert(True), s.cipher()
s.write("GET / HTTP/1.1\r\nHost: " + host + "\r\n\r\n")
print s.read()
s.close()