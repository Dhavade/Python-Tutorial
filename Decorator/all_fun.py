# -*- coding: utf-8 -*-
"""
Created on Thu May 13 12:19:17 2021

@author: Admin
"""
def only_int_alloy(fun):
    def wrapper(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return fun(*args,**kwargs)
        else:
            print("invalid argument")
        '''data_type=[]
        for arg in args:
            data_type.append(type(arg)==int)
        if all(data_type):
            return fun(*args,**kwargs)
        else:
            print("invalid argument")'''
    return wrapper        


@only_int_alloy
def and_all(*args):
    total=0
    for i in args:
        total+=i
    return total


print(and_all(1,2,3,4,5,[1,2,3]))     