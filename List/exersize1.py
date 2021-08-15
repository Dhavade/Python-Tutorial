# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:21:15 2021

@author: Admin
"""

def l(p):
    b=[]
    for i in range(len(p)):
        a=p.pop()
        b.append(a)
    return b

num=[1,2,3,4]
print(l(num))
    