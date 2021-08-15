# -*- coding: utf-8 -*-
"""
Created on Tue May 11 13:23:29 2021

@author: Admin
"""

#def p(*args):
 #   a=[]
  #  for i in zip(*args):
   #     a.append(sum(i)//len(i))
    #return a

p=lambda *args:[sum(i)//len(i) for i in zip(*args)]

d=[[1,2,3],[3,4,5],[4,5,6]]
print(p(*d))    