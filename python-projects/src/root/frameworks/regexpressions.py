'''
Created on Sep 12, 2014

@author: lada
'''
#python library, chapter 7, re
import re

#gives first occurrence
a="adit12asd 45 dsf 67 daf64"
m = re.search(r'\d+', "adit12asd")
print m.start(), m.end(), m.group()

pattern = re.compile(r'\d')
m1 = pattern.search("100")
print m1.group()

#finding/iterating numbers
numbers = re.compile(r'\d+')
for m in numbers.finditer(a):
    print m.group()
    
#substitution
s = re.sub(r"\d+", "-", a)
print s

#replace only first 3 occurrences
s = re.subn(r"\d+", "-", a,3)
print s