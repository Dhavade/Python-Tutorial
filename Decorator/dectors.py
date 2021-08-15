# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:30:08 2021

@author: Admin
"""

# decorators

def p(a):
    return a**2

#print(p(3))
d=p
print(d(7))
print(d.__name__)
print(p.__name__)