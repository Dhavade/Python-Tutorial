# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:32:40 2021

@author: Admin
"""
from functools import wraps
def print_function_data(fun):
    @wraps(fun)
    def warrper(*args,**kwargs):
        print(f"you are colling {fun.__name__} function")
        print(f"{fun.__doc__}")
        return fun(*args,**kwargs)
    return warrper



@print_function_data
def add(a,b):
    '''this function takes two number as argument and return there sum'''
    return a+b

print(add(3,4))

'''
otu-
you are colline add function
this function takes two number as argument and return there sum
7
'''
