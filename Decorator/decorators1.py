# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:25:12 2021

@author: Admin
"""

#decorators - enhance tha functionality of other function

# @ use for decorators

def decoretoe_fun(any_fun):
    def waepper_fun():
        print("this is function")
        any_fun()
    return waepper_fun    





def fun1():
    print("this is awsome function")
var=decoretoe_fun(fun1)
var()    


@decoretoe_fun    
def fun2():
    print("this is awsome function")    

fun2()



    
#fun1()
#fun2()