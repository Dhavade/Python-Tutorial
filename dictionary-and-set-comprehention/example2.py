# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:53:59 2021

@author: Admin
"""

# dictionary comprehention with if else
# {1:'odd',2:'even}

d={num:('even' if num%2==0 else 'odd') for num in range(1,11)}
print(d)

a={i:i**3 for i in range(1,11)}
print(a)

c=[i**3 if (i%2==0) else (-i) for i in range(1,11)]
print(c)

q={i**3 for i in range(1,11)}
print(q)
