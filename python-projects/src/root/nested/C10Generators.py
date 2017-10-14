'''
Created on Sep 6, 2014

@author: lada
'''
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in xrange(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
    print "And the next number is... %d!" % random_number
    
# fill in this function
def fib():
    a,b = 1,1
    for x in xrange(12):
       # print "x is %d" % x
        if x == 0 or x == 1:
            yield a
        else:
            yield(a+b)
            a,b = b,a+b
    
    

# testing code
import types
if type(fib()) == types.GeneratorType:
    print "Good, The fib function is a generator."

    counter = 0
    for n in fib():
        print n
        counter += 1
        if counter == 12:
            break