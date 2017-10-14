'''
Created on Sep 10, 2014

@author: lada
demo of deepcopy to copy deep structures
'''
from copy import deepcopy
a=[10,20,[30,40],50]
b=list(a)
c=deepcopy(a)
print a,b,c
a[2][1] = 100
b[2][1] =200
print a,b,c