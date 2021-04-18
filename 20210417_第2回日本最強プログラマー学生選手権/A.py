#!/usr/bin/env python
# coding: utf-8

# In[4]:


X, Y, Z = map(int, input().split())

YZ = Y * Z

if YZ % X == 0:
    print(int(YZ / X)-1)
elif YZ / X <= 1:
    print(0)
else:
    print(int(YZ / X))
