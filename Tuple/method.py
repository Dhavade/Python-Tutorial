# -*- coding: utf-8 -*-
"""
Created on Fri May  7 23:10:37 2021

@author: Admin
"""
mixed=(1,2,3,4,5)
print(type(mixed))
for i in mixed:
    print(i)
    
    
num=(1,)
print(type(num))

name=("pranay","prakash","dhavade")
p,q,r=name
print(p)    


#list inside tuple
p=("pranat",[1,2,3,4])
p[1].pop()
print(p)
print(p)
p[1].insert(2,2)
print(p)

