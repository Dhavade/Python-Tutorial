# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:16:09 2021

@author: Admin
"""

a=[]
b=[]
c=[]
n=int(input("enter tha number "))
for i in range(0,n):
    number=int(input(""))
    a.append(number)
    print(i)
    if i%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
        
b=sorted(b)
print("sorted even array",b[0:len(b)])
c=sorted(c)
print("sorted odd array",c[0:len(c)])
print(b[-2]+c[1])
        
print(n)        
print(a)
print(b)
print(c)        