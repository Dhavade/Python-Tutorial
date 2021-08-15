# -*- coding: utf-8 -*-
"""
Created on Sat May  8 12:27:47 2021

@author: Admin
"""

# example
#cube_finder(3)
#{1:1,2:8,3:27}

def d(l):
    dish={}
    for i in range(1,l+1):
        dish[i]=i**3
    return dish

print(d(3))    