'''
Created on Sep 10, 2014

@author: lada
'''
def greet(m, user):
    print m(user)
    
welcome = lambda x: "Welcome to python, " + x

greet(welcome, "Spiderman")

a = [2,3,4,6,5,7,8]

#use of map and lambda, functions on the fly
for asd in a:
    b = map(lambda x: x*x,a)
    
print b


names = ('john','sam','jonathan','ram','dave')

c = map(lambda x: x.capitalize(), names)
print c

n = filter(lambda x: x[0] in 'jJ', names)
print n