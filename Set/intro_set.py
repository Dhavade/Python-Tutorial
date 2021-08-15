# -*- coding: utf-8 -*-
"""
Created on Sat May  8 22:33:11 2021

@author: Admin
"""

# set is data type
#set is unordered collections of item

s={1,2,3,4,5,6}
print(s)

l=[1,2,3,4,5,6,2,3,4,6,7,5,1]
print(l)
e=set(l)
print(e)
print(list(e))

s.add(7)
print(s)

s.remove(3)
print(s)

s.discard(8)
print(s)

p={1,2,3,4}
p.clear()
print(p)
g={1,2}
g.copy()
print(g)


s={1,2,'string',1.2,('S',)}
print(s)
s.pop()
print(s)















