# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:05:42 2021

@author: Admin
"""

def p(name='pranay',age=23):
    print(name)
    print(age)
    
p('rahul')    


def a(name,*args,name_1='pranay',**kwargs):
    print(name)
    print(args)
    print(name_1)
    print(kwargs)
    
a('pranay',1,2,3,a=1,b=3)    