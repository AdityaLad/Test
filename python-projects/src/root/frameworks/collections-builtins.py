'''
Created on Sep 9, 2014

@author: lada

Usage of zip, izip, enumerate 
 
'''
from itertools import izip
names = ("Aa", "bb", "cc", "dd")
ages = (11,22,33,44)

#izip id replacement for zip which has poor performance
for name, age in izip(names,ages):
    print name, age

#zip    
for name, age in zip(names,ages):
    print name, age

#Enumerators, when u want to print index as well    
for i,n in enumerate(names): print i,n