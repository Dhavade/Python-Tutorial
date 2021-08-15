# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:48:32 2021

@author: Admin
"""

# kwargs (keyword argument)
# **kwargs (double star operator)

def p(**kwargs):
    for k, w in kwargs.items():
       print(f"{k}:{w}")
    
a={'name':'pranay','age':24}    
p(**a)   