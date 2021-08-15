# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:55:54 2021

@author: Admin
"""

# min , max function adavance

p=[1,2,3,4,5]
print(max(p))
print(min(p))

name=['pranay dhavade','raj','rahul','pranav']
print(max(name,key=lambda item:len(item)))

student1=[
    {'name':'pranay','score':90,'age':24},
    {'name':'mohit','score':80,'age':36}
]

print(max(student1,key = lambda item:item.get('score'))['name'])

student2={
    "pranay":{"score":49},
    "rahul":{"score":57}
    }

print(max(student2,key = lambda item:student2[item]['score']))