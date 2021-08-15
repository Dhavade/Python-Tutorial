# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:23:11 2021

@author: Admin
"""

p=[]
for i in range(3):
    for i in range(1,4):
        p.append(i)
print(p)    

l=[[i for i in range(1,4)] for i in range(3)]
print(l)