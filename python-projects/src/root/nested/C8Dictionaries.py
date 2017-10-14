'''
Created on Sep 6, 2014

@author: lada
'''
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here

if "Jake" in phonebook:
    print "Jake is listed in the phonebook."
if "Jill" not in phonebook:
    print "Jill is not listed in the phonebook."
    
for name, id in phonebook.iteritems():
    print "The id associated with name : %s is %d " % (name,id)
    
phonebook.pop("John");
print "----"
for name, id in phonebook.iteritems():
    print "The id associated with name : %s is %d " % (name,id)
    
del phonebook["Jack"] 
print "----"   
    
for name, id in phonebook.iteritems():
    print "The id associated with name : %s is %d " % (name,id)

#tuples    
names = ('a','b','c')
ages = (10,20,30)

#creating dictionary by combining tuples, but this does not maintain order of keys in names
info = dict(zip(names,ages))

for v in info.itervalues(): print v
for k in info.viewkeys(): print k, info[k]

from collections import OrderedDict
d = OrderedDict(zip(names,ages))
for items in d: print items,d[items]