 # -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:41:49 2021

@author: Admin
"""

# map() function

num=[1,2,3,4]

#def a(l):
 #   return l**2

b=list(map(lambda l: l**2,num))
print(b)

c=[i**2 for i in num]
print(c)

p=[]
for j in num:
    p.append(j**2)
print(p)

name=['pranay','raj','rajil']
length=map(len,name)
for i in length:
    print(i)
    
