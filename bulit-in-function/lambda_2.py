# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:04:43 2021

@author: Admin
"""

# lambda expretions practice

def a(l):
    return l%2==0

print(a(2))
#------------------------------------------------------ 

a=lambda l:l%2==0
print(a(2))
#------------------------------------------
b=lambda b:b[-1]
print(b('pranay'))
#------------------------------------------------
def p(l):
    return len(l)>4
       
    
print(p('pranay'))

p=lambda l:True if len(l)>4 else False
print(p('rahul'))
    