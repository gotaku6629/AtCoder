#!/usr/bin/env python
# coding: utf-8

# In[7]:


N = int(input())
A = list(map(int, input().split()))

A.sort() # N^{5}

Q = [0 for i in range(N)]
Q[0] = A[0]
for i in range(1, N):
    Q[i] = A[i] - A[i-1]

sum = 1
for i in range(N):
    sum *= (Q[i]+1)
print(sum)


# In[ ]:




