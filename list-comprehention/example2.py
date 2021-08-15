# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:34:41 2021

@author: Admin
"""

def p(l):
    a=[]
    for i in l:
        a.append(i[::-1])
    return a

print(p(['abc','cdr','gfh']))    

def p(l):
    return [i[::-1] for i in l]

print(p(['abc']))