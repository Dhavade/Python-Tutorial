# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:37:00 2021

@author: Admin
"""
import random
winning_number=random.randint(1, 100)
guess=1
number=int(input("guess tha number between 1 to 100 : "))
game_over=False

while not game_over:
     if number==winning_number:
          print(f"you are correct guess ! : tou win !!! {guess} times")
          game_over=True
     else:
         if number<winning_number:
            print("higher number plese")
            guess+=1
            number=int(input("guess again :"))
         else:
            print("lower number plese")
            guess+=1
            number=int(input("guess again :"))