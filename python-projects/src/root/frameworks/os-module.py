'''
Created on Sep 8, 2014

@author: lada
https://docs.python.org/2/library/os.html
'''
import os

filename="C:\eula.1028.txt"
#removes a file
#os.unlink("tets")
print os.getcwd()
print os.open(filename, os.F_OK)
print "Hello"

file2="C:\eula.1028.txt"

if os.path.exists(file2):
    print "File exists"
else:
    print "File does not exist"