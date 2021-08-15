# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:13:50 2021

@author: Admin
"""

num=[1,2,3,4,5,6,7,8,9,10]

num1=[]
for i in num:
    if i%2==0:
        num1.append(i**2)
    else:
        num1.append(-i)
print(num1) 

num2=[i**2 if(i%2==0) else(-i) for i in num] 
print(num2)      