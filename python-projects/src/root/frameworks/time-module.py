'''
Created on Sep 9, 2014

@author: lada
Example of time module for calculation of time taken for execution
 and sleep method to introduce delays.
'''
import time
from time import sleep

start = time.clock()
sleep(1)

for x in xrange(10000):
    pass

end = time.clock()

print end - start
    