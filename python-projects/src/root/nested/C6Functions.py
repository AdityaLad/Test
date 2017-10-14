'''
Created on Sep 1, 2014

@author: lada
'''
def my_function():
    print "This is an empty function"

def my_function_with_args(arg1, arg2):
    print "Hello %s, Its has been %s"%(arg1,arg2)
    
def sum_two_numbers(num1, num2):
    return num1 + num2
# print a simple greeting 
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print x

print "The sum of 2 and 4 is %d" % sum_two_numbers(2, 4)