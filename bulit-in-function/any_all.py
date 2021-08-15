# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:38:02 2021

@author: Admin
"""

# any , all function

num1=[1,2,4,6,8]

p=any([num%2==0 for num in num1])
print(p)

p=all([num%2==0 for num in num1])
print(p)
