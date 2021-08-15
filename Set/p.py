# -*- coding: utf-8 -*-
"""
Created on Sat May  8 22:48:28 2021

@author: Admin
"""
# if and else stestment in set
s={1,2,3,4}


if 1 in s:
    print("present")
else:
    print("absent")

for i in s:
    print(i) 
    
    
    
a={1,2,3,4,5}
b={1,2,3,6,7}    

#union
#intersection

union_set=a|b
print(union_set)


intersection_set=a&b
print(intersection_set)

