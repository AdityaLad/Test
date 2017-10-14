'''
Created on Sep 9, 2014

@author: lada
'''
f = open("test.txt", "w")
f.write("Hello world my file.\n")
print >>f, "Hello from print"
f.close()

print "###Reading our file####"
f = open("test.txt", "r")
print f.read()
f.close()

with open("b.txt", "w") as f:
    f.write("this is another file, where we do not have to close the fd\n")
    print >>f, "Hello by print"

print "###Reading our file, file object is an iterable object####"
f = open("b.txt", "r")
for line in f:
    print line.strip()
f.close()
