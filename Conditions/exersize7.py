# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:38:46 2021

@author: Admin
"""

name=input("enter your name")
#pranay dhavade
i=0
temp_var=""
while i<len(name):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1
    