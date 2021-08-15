# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:46:59 2021

@author: Admin
"""

#map
#def squre(l):
 #   return l**2

a=[1,2,3,4,5]
#print(list(map(lambda l:l**2,a)))

#-------------------------------------------------------

def my_map(fun,l):
    b=[]
    for i in l:
       b.append(fun(i))
    return b

    
print(my_map(lambda b:b**2,a))

def my_list2(fun,l):
    return [fun(i) for i in l]
  

