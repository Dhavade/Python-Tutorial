# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:04:59 2021

@author: Admin
"""

# function returnig function
'''
def outer_fun():
    def inner_fun():
        print("hello pranay")
    return inner_fun

var=outer_fun()
var()  
'''
def outer_fun(msg):
    def inner_fun():
        print(f"massage is {msg}")
    return inner_fun

var=outer_fun("hi")
var()    