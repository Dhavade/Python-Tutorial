# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:11:34 2021

@author: Admin
"""

def p(l,j):
    a=[]
    for i in l:
        if i in j:
            a.append(i)
    return a        

                

print(p([1,2,3,4],[2,1,6,7]))           