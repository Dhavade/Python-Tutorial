# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:44:38 2021

@author: Admin
"""

def p(*l):
    if all([(type(a)==int or type(a)==float) for a in l]):
        total=0
        for i in l:
           total+=i
        return total
    else:
        return 'wrong input'

print(p(1,1,1,1.3))   

a=(3.4,4.5)
print(sum(a))