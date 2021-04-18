#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
A, B = map(int, input().split())

for c in range(B, 0, -1):
    if (B // c) - ((A-1)//c) >= 2:
        print(c)
        break


