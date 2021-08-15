# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:55:36 2021

@author: Admin
"""

def p(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]

print(p([1,2,1.3,'pranay','raj']))