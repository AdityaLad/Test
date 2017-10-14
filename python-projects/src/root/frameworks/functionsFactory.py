'''
Created on Sep 11, 2014

@author: lada
Factory pattern for construction and returning of functions
'''
def foo():
    print "inside foo"
    def bar():
        print "inside bar"
    return bar


b = foo()
b()

####
def buy(v=None):
    if v == "car":
        def vehicle(): print "Driving car..."
    elif v == "bike":
        def vehicle(): print "Riding bike..."
    else:
        def vehicle(): raise TypeError, "Invalid vehicle type..."
    return vehicle

c = buy("car")
c()
b = buy("bike")
b()
