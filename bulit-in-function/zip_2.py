# -*- coding: utf-8 -*-
"""
Created on Tue May 11 13:11:53 2021

@author: Admin
"""

# * operator with zip

l=[1,3,4,6]
b=[3,6,1,9]

a=[(1,3),(3,6),(4,1),(6,9)]
l,b=list(zip(*a))
print(l)
print(b)

s=[]
for i in zip(l,b):
    s.append(max(i))
print(s)    
print(tuple(s))
print(set(s))