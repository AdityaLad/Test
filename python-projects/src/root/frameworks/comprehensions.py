'''
Created on Sep 10, 2014

@author: lada
'''

nums = [1,2,3,4,5,6,78,40]
#result = map(lambda x: x*x, nums)
#Using comprehensions, its a different kind of fop loop
result = [ x*x for x in nums ]
print result

names = ('john','sam','jonathan','ram','dave')

v = tuple(n.upper() for n in names)
print v

#store square of even numbers, combination of maps and filter
zz = [x*x for x in nums if x%2 == 0]
print zz

#this will give a generator object
ansxx = ( x*x for x in nums)
print type(ansxx)

for ab in ansxx: print ab,
    