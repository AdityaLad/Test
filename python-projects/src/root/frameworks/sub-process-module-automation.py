'''
Created on Sep 12, 2014

@author: lada
'''
from subprocess import Popen
p = Popen(["ls", "-l"])
ret = p.wait()

print "Ret = ", ret

from os import system
system("ls -l")

from os import fork, execve, wait

pid = fork()
