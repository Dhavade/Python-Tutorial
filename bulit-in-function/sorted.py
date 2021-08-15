# -*- coding: utf-8 -*-
"""
Created on Wed May 12 11:15:07 2021

@author: Admin
"""

# sorted function

l=[2,1,5,4,3]
l.sort()
print(l)

p=(2,1,3,4)
pr=sorted(p)
print(pr)

a={'pranay','rah','jshs'}
print(type(a))
print(sorted(a))

guitars=[
    {'model1':'yamaha','price':4300},
    {'model':'hero','price':3700},
    {'model':'faylor','price':4799}
    ]

print(sorted(guitars,key=lambda d:d['price'],reverse=True))



