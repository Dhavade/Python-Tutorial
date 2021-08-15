# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:16:54 2021

@author: Admin
"""

#function return function (closure) function

def outer(x):
    def inner(n):
        return n**x
    return inner

cube=outer(3)
print(cube(2))

squre=outer(2)
print(squre(2))