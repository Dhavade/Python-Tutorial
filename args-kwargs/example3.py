# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:51:13 2021

@author: Admin
"""

def p(l):
    mul=1
    for i in l:
        mul*=i
    return mul


print(p([1,2,3]))