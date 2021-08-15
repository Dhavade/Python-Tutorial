# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:13:21 2021

@author: Admin
"""
from functools import wraps 
def decoratoe_fun(any_fun):
    @wraps(any_fun)
    def wapper_fun(*args,**kwargs):
        '''this is warpper fun'''
        print(f"this is awsome fun{wapper_fun.__doc__}")
        return any_fun(*args,**kwargs)
    return wapper_fun

@decoratoe_fun
def fun1():
     '''this is fun'''
     print("a")
fun1()     
     
print(fun1.__doc__)  
print(fun1.__name__) 
