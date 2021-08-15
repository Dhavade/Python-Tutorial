# -*- coding: utf-8 -*-
"""
Created on Sat May  8 12:38:39 2021

@author: Admin
"""


def d(l):
    c={}
    for i in l:
        print(i)
        c[i]=l.count(i)
    return c

print(d('pranayA'))    