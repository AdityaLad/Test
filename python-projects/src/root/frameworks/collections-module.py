'''range()
Created on Sep 10, 2014

@author: lada
deque is implemented as a doubly linked circular list
'''
from collections import deque
d = deque()
a = [1,2,3,4]
b = deque(a)
b.pop()
b.popleft()

d.append(12)
d.appendleft(0)
d = deque(range(10,100,10))

d.rotate()
d.rotate(-1)

from collections import OrderedDict

from collections import Counter
#counter can be operated on a list or tuple
str = "this is a test is is is a test is this a test with some test words"
count = Counter(str.split())
print count