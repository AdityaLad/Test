'''
Created on Sep 10, 2014

@author: lada
'''
"""
Write a program to print all indices of substring occurring in
a main string.

Synopsis
--------
>>> find_all(line, "test")
10 20 28 33 49

"""
line = "this is a test is a test is test test words with test words"

def find_all(main_string, sub_string):
    i=0
    while(True):
        i = main_string.find(sub_string, i)
        if i == -1: break
        print i
        i = i + len(sub_string)

m = raw_input("Enter a string: ")
s = raw_input("Enter a substring: ")

find_all(line, "test")

