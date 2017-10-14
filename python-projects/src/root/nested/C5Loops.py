'''
Created on Sep 1, 2014

@author: lada
'''
'''
Example 1 : iterate over a list
'''
primes = [2, 3, 5, 7]
for prime in primes:
    print prime
    

'''
Example 2: go over a range
'''
# Prints out the numbers 0,1,2,3,4
for x in xrange(5): # or range(5)
    print x

# Prints out 3,4,5
for x in xrange(3, 6): # or range(3, 6)
    print x

# Prints out 3,5,7
for x in xrange(3, 8, 2): # or range(3, 8, 2)
    print x
    
    
'''
Example 3: while loops
'''
# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print count
    count += 1  # This is the same as count = count + 1
    
'''
Example 4: Break and continue 
'''
    # Prints out 0,1,2,3,4

count = 0
while True:
    print count
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in xrange(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print x