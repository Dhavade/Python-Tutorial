# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:42:51 2021

@author: Admin
"""

def p(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

mixed= [1,2,[3,4],[3,4]]
print(p(mixed))       