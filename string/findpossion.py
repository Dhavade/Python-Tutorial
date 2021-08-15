# -*- coding: utf-8 -*-
"""
Created on Mon May  3 21:01:33 2021

@author: Admin
"""

string=" he is beutiful and he is smart"
print(string.replace("is","was",1))

is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)