'''
Created on Sep 6, 2014

@author: lada
Create a new list out of an existing list that contains only positive numbers
'''

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []

for num in numbers:
    if num > 0:
        newlist.append(num)

print newlist

#copy a list
a = numbers[:]
b = list(numbers)

print a,b