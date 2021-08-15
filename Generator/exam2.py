# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:41:11 2021

@author: Admin
"""

#def num(n):
 #   print(list(i for i in range(1,n+1) if i%2==0 ))
    
#num(5)  
#num(10)

def num(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
            
            
#print(num(10))
number=num(10)            
for i in number:
    print(i)
    
for i in number:
    print(i)    