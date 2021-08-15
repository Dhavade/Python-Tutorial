# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:35:06 2021

@author: Admin
"""

def p(num,*args):
    if args:
        return [i**num for i in args]
    else: 
        return ("you didnt pass any args")
    
num=[1,2,3]
print(p(3,*num))    
        