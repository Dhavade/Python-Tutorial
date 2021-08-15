# -*- coding: utf-8 -*-
"""
Created on Sat May  8 11:36:20 2021

@author: Admin
"""


   # add and delet

user={
      "name":"pranay",
      "age":24,
      "fav movies":["coco","kimi no na wa"],
      "fav song":["kkwe"]
      }

#how to add

user["name"]=["pratik"]
print(user)


#how to delet using pop method

user_item=user.pop("age")
print(user)

#popitem method

popped_item=user.popitem()
print(user)
print(popped_item)
