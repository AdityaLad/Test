'''
Created on Sep 12, 2014

@author: lada
'''
from time import sleep
from threading import Thread

def foo():
    for x in xrange(5):
        print "Foo: ", x
        sleep(1)
        
def bar():
    for x in xrange(5):
        print "Bar: ", x
        sleep(1)
        
t1 = Thread(target=foo)
t2 = Thread(target=bar)

t2.daemon = True
t1.start()
t2.start()

#t1.join()
#print "t1 finished"
#t2.join()
#print "t2 finished"

for x in xrange(7):
    print "Main thread", x
    sleep(1)