# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:34:22 2021

@author: Admin
"""

name=input("enter tha name")
temp= ""
for i in range(len(name)):
    if name[i] not in temp:
        temp+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
        
        

