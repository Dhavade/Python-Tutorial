# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:18:46 2021

@author: Admin
"""

# enumerate function
# using for loop

l=['abc','dheudheu','def']
# output
#0------->abc
#1-------->def
#2-------->dheudheu

#pos=0
#for name in l:
 #   print(f"{pos}---->{name}")
  #  pos+=1
    
    
    
# using enumerate function

#for pos,name in enumerate(l):
#    print(f"{pos}------->{name}")



def p(l,target):
    for pos,name in enumerate(l):
        if name==target:
           return pos
    return -1

print(p(l,'def'))    
    











