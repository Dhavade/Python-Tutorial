# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:53:39 2021

@author: Admin
"""

#number=list(range(1,11))
#print(number)


number=[1,2,3,4,5,6,7,8,9,10]

def p(l):
    negative=[]
    for i in number:
        negative.append(-i)
    return negative

print(p(number))