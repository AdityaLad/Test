'''
Created on Sep 12, 2014

@author: lada
'''
from multiprocessing import Pool
from mutliprocessing.managers import BaseManager
#RPCs in python

class MyManager()BaseManager: pass
MyManager.register('Maths', MathsClass)

import time
def fibo(x):
    a,b=0,1
    for i in range(x):
        yield a
        a,b=b,a+b
        
x = xrange(400)

p = Pool(16)
start = time.clock()
p.map(fibo, x)
d = time.clock() - start
print d