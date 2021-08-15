# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:43:37 2021

@author: Admin
"""

def decorator_fun(any_fun):
    def warpper_fun(*args,**kwargs):
        print("this is awosome")
        return any_fun(*args,**kwargs)
    return warpper_fun

@decorator_fun
def fun_1(a):
    print(f"this is fun1 {a}")    
    
fun_1(3)


@decorator_fun
def fun2(a,b):
    return a+b

print(fun2(2,3))




    