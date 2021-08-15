# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:16:49 2021

@author: Admin
"""

 #list comprehention
 #with tha help tha list comprehention we can create of list in one line

# create a list of squre from 1 to 10
l=[]
for i in range(1,11):
     l.append(i**2)
print(l)    


l=[i**2 for i in range(1,11)]
print(l)

#p=[]
#for i in range(1,11):
 #   p.append(-i)
#print(p)    

p=[-i for i in range(1,11)]
print(p)


k=['pranay','rahul','raj']
c=[]
for i in k:
    c.append(i[0])
print(c)



c=[i[0] for i in k]
print(c)













    
    