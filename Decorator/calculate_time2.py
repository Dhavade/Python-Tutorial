# -*- coding: utf-8 -*-
"""
Created on Thu May 13 12:01:36 2021

@author: Admin
"""

#from functools import wraps
import time

def calculate_time(fun):
   # @wraps(fun)
    def wrapper(*args,**kwargs):
        print(f"excutint ....{fun.__name__}")
        t1=time.time()
        return_volue=fun(*args,**kwargs)
        t2=time.time()
        total=t2-t1
        print(f"this function tooks {total} secound")
        return return_volue
    return wrapper

@calculate_time
def p(n):
    return[i**2 for i in range(1,n+1)]

p(1000)

