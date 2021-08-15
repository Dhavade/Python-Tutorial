# -*- coding: utf-8 -*-
"""
Created on Sat May  8 11:11:12 2021

@author: Admin
"""

user={
      "name":"pranay",
      "age":24,
      "fav movies":["coco","kimi no na wa"],
      "fav song":["kkwe"]
      }

if "name" in user:
    print("present")
else:
    print("absent") 
    
    
if "pranay" in user.values():
    print("present")
else:
    print("absent")  
    
for i in user:
    print(i)
    
    # or
    
for i in user:
    print(user[i])    

for i in user.values():
    print(i) 
    
    
for key,value in user.items():
    print(f"tha key is {key} and values is {value}")    
    
    
    
    
    
    
    
    
    
    
    
       