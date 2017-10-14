'''
Created on Sep 9, 2014

@author: lada
'''
def is_prime(x):
    for i in xrange(2, x/2):
        if ( x % i) == 0:
            return False            
    else:
        return True
        
num = input("Enter numbers to generate:")
count =0
y = 2

while (count < num):
    if is_prime(y):
        print y
        count = count + 1
    y = y + 1
