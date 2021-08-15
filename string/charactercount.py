# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:47:00 2021

@author: Admin
"""

name="         pranay        "
dots="...................."
a=name+dots
print(a)

print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
print(name.replace(" ", ""))


name, char=input("enter your name and characters  :").split(",")
print(f"length of your name{len(name)}")
print(f"count character : {name.strip().lower().char.count(name)}")