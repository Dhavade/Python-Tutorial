# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:49:24 2021

@author: Admin
"""

# iterator and iterables

num=[1,2,3,4,5] # tuple,string ----->iterables
squares=list(map(lambda a:a**2,num)) #iterator

print(squares)
#print(next(squares))