# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:45:50 2021

@author: Admin
"""

number=list(range(1,11))
print(number)

a=[]
for i in number:
    if i%2==0:
        a.append(i)
print(a)    

b=[i for i in number if i%2==0]
print(b)

c=[i for i in range(1,11) if i%2==0]
print(c)