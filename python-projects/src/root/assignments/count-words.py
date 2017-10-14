'''
Created on Sep 10, 2014

@author: lada
'''
a = "this is a test is is is a test is this a test with some test words"

def count_words(arg):
    info = {}
    words = arg.split(" ")
    for word in words:
        info[word] = info.get(word,0) + 1
                
    for k in info:
        print k,info[k]
            
count_words(a)