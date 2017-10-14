'''
Created on Sep 6, 2014

@author: lada
'''
def do_stuff_with_number(n):
    print "Bad choice %d" % n

the_list = (1, 2, 3, 4, 5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError: # Raised when accessing a non-existing index of a list
        do_stuff_with_number(0)