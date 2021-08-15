# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:28:57 2021

@author: Admin
"""

# filter function

#def p(l):
  #  return l%2==0

number=[1,2,3,4,5,6,7]
even=tuple(filter(lambda i:i%2==0,number))
print(even)

for i in even:
    print(i)
    
number=[1,2,3,4,5,6,7]
even=tuple(map(lambda a:a%2==0,number))
print(even)



def a(*l):
        return i%2==0
       
        
print(a(1,2,3,4))        
    
