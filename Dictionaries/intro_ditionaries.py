# -*- coding: utf-8 -*-
"""
Created on Sat May  8 10:44:39 2021

@author: Admin
"""

# dictionaries intro
#Q-whay we  use dictionaries
#A-beacause of limitation of lists , lits are not  enogh to represent
# real data-

# example
user=["hatshit","pranay",24,["coco","kimi no na wa"],["awankini"]]
#this lists contain user name,age,fav movies,fav tunes
# you can do this but this is not a good way to do this



#Q-what are ditionaries
#A-ditionaries is unordered collections of data in key : value pair

#  how to create ditionaries

user={"name":"pranay","age":24}
print(user)
print(type(user))

user={
      "name":"pranay",
      "age":24,
      "fav movies":["coco","kimi no na wa"],
      "fav song":["kkwe"]
      }


user1=dict(name="pranay",age=24)
print(user1)
print(user["name"])

user2={}
user2["name"]="pranay"
print(user2)
