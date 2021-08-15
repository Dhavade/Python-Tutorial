# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:52:53 2021

@author: Admin
"""

number=[1,3,4,5,6]
print(number[1:4])
print(number.pop())
number.append(8)
print(number)

word=["woed1","word2","word3"]
print(word[:2])


mixed=[1,2,3,4,"five","six",2.3,None]
print(mixed[-1])

mixed[1:]=["three","four"]
print(mixed)