 # -*- coding: utf-8 -*-
"""
Created on Sat May  8 11:56:12 2021

@author: Admin
"""

#fromkeys method

d=dict.fromkeys(["name","age"],("pranay","radhe"))
print(d)

d=dict.fromkeys(("name","age"),("pranay","radhe"))
print(d)

d=dict.fromkeys(("age"),("pranay","radhe"))
print(d)

d=dict.fromkeys(range(1,11),("pranay","radhe"))
print(d)

# get method (useful)

d={'name':'pranay','age':24,'fav song':'hindi'}
print(d['name'])
print(d.get('name'))

if 'names' in d:
    print('present')
else:
    print('not present')  
    
    
    
if d.get('name'):
    print('present')
else:
    print('not present')  
    
        

#d.clear()
#print(d)


d1=d.copy()
print(d1)

print(d.popitem())
print(d1)










    