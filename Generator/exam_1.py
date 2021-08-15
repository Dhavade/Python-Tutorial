# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:13:36 2021

@author: Admin
"""



# generator

def num(n):
    for i in range(1,n+1):
        yield(i)
    
number=num(10)    
#print(num(10)) 
for numb in number: 
    print(numb)  
    
    
    
for numbe in number: 
    print(numbe)      