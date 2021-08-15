# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:47:59 2021

@author: Admin
"""

# lamda expretions (anonymous function)

def a(b,c):
    return b+c

print(a(1,2))

add1=lambda b,c :b+c
print(add1(2,3))

add2=lambda a,b:a*b
print(add2(2,3))

print(add1)
print(add2)
print(a)