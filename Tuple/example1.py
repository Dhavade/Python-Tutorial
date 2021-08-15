# -*- coding: utf-8 -*-
"""
Created on Fri May  7 23:26:17 2021

@author: Admin
"""

a=[]
b=[]
c=[]
n=int(input("enter tha number"))
for i in range(0,n):
    number=int(input(""))
    a.append(number)
    if i%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
print(a)  
print(b)
print(c)  