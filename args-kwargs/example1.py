# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:25:20 2021

@author: Admin
"""

# make flexible function

#*operator
#*args

#def p(a,b):
 #   return a+b

#print(p(1,2))

def p(num,*args):
    total=0
    for i in args:
        total+=i
    return total

print(p(1,2,3))    

def a(l):
    total=0
    for i in l:
        total+=i
    return total    
print(a((1,2,3)))        