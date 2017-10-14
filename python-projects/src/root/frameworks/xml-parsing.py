'''
Created on Sep 12, 2014

@author: lada
'''
import xml.etree.ElementTree as xml
from urllib2 import urlopen
rss_url = "http://toi.timesofindia.indiatimes.com/rssfeedstopstories.cms"

f = urlopen(rss_url)

contents = f.read()

rootElement = xml.fromstring(contents)

for item in rootElement.findall("channel/item"):
    print "-"*20
    print item.find("title").text 
    print "-"*20
    print item.find("description").text 