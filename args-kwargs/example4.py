# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:27:39 2021

@author: Admin
"""

def i(*args):
    total=1
    for i in args:
        total*=i
    return total


p=[1,2,3] 
print(i(*p))   