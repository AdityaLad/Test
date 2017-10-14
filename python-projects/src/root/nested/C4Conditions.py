'''
Created on Sep 1, 2014

@author: lada
'''
from _sqlite3 import Statement
'''
Example 1
'''
x = 2
print x == 2 # prints out True
print x == 3 # prints out False
print x < 3  # prints out True

'''
Example 2
'''
name = "John"
age = 23
if name == "John" and age == 23:
    print "Your name is John, and you are also 23 years old."

if name == "John" or name == "Rick":
    print "Your name is either John or Rick."
    

'''
Example 3: The in operator
'''
if name in ["John", "Rick"]:
    print "Your name is either John or Rick."
    
'''
Example 4: The if-else operator
'''
x = 2
if x == 2:
    print "x equals two!"
else:
    print "x does not equal to two."
'''
Example 5: The elif operator
'''
if x == 3:
    print "x is 3"
elif x == 2:
    print "x is 2"
else:
    print "I don know fucking x of urs"
    
'''
Example 6: The is/== operator difference, checking on the equality of object instances
'''
x = [1,2,3]
y = [1,2,3]
print x == y # Prints out True
print x is y

    
'''
Example 7: The not operator 
'''
print not False # Prints out True
print (not False) == (False)

'''Example 8: Too much of if Statement
'''
x,y=1,2
a,b=11,12
if (x == 1 and a == 10) and (b == 12  and y == 2):
    print 'Both true'
else:
    print "Both false"