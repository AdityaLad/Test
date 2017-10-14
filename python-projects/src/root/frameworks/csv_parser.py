'''
Created on Sep 12, 2014

@author: lada
'''
import csv

with open(file) as f:
    records = csv.reader(f)
    for name, age, loc in records:
        print name, age, loc