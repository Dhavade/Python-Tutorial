# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:08:22 2021

@author: Admin
"""

winning_number=55
num=input("guess a number\n")
num=int(num)
if num==winning_number:
    print("you guessed correctly 'you win !!!'")
else:
    if num>winning_number:
         print("plese guess lower number plese")
         
    else:
         print("you guess higher number plese")
        
         