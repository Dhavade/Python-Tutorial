# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:21:26 2021

@author: Admin
"""

name=input("enter your name")
temp= ""
i=0
while i<len(name):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1