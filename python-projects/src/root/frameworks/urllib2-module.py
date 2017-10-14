'''
Created on Sep 8, 2014

@author: lada
'''
import urllib2

response = urllib2.urlopen("https://python.org/")
headers = response.info()
print headers

statuscode = response.getcode()

print statuscode

html = response.read()
#print html