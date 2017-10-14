'''
Created on Sep 11, 2014

@author: lada
the only purpose of init method is to initialize instance variables
'''
'''        
     def __init__(self, name="Honda", *args, **kwargs):
        self.name = name
'''
class Car:
#constructor    
    def __init__(self, name="Honda"):
        self.name = name
               
    def drive(self):
        print "Drive car", self.name
#destructor
    def __del__(self):
        print "Car object destroyed.."
                
c1 = Car("Toyota")
c2 = Car("Nissan")
c3 = Car()
c1.drive()
c2.drive()
c3.drive()
