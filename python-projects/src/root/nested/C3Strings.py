'''
Created on Sep 1, 2014

@author: lada
'''
astring = "Hello world! But this is my love"
print "Length of string: %d" % len(astring)
print astring.index("o")
print astring.upper()
print "=== %d" % astring.find("llko")
print astring[3:7]
abrokenway = astring.split(" ");
print abrokenway[3]
for x in abrokenway:
    print x
