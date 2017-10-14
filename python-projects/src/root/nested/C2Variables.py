'''
http://www.learnpython.org/en/Welcome

Created on Aug 31, 2014

@author: lada
'''

'''
Basic variables
'''
mystring = "hello"
myfloat = 10.0
myint = 20


if mystring == "hello":
    print "String: %s" % mystring
if isinstance(myfloat, float) and myfloat == 10.0:
    print "Float: %d" % myfloat
if isinstance(myint, int) and myint == 20:
    print "Integer: %d" % myint

'''
Lists
'''
numbers = [1,2,3]
strings = ["A", "b"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = "nABY"

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers[2])
print(strings)
for x in names:
    print x
print("The second name on the names list is %s" % second_name)

'''
Examples of print formatting
'''
# This prints out "John is 23 years old."
name = "John"
age = 23
print "%s is %d years old." % (name, age)
print name + " is %d years old." % (age)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %s$."

print format_string % data

#List and tuples
#Tuples () and Lists [] - modifieable collection