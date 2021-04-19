#!/usr/bin/env python
# coding: utf-8

# In[ ]:


A, B = map(int, input().split())
 
# 大きいほうを取る
X = A #  X:大きい
Y = B #  Y:小さい
flag = 0
if A < B:
    flag = 1
    X = B
    Y = A
 
list1 = [i+1 for i in range(X)]
list2 = [i for i in range(X-Y+1, X+1)]
L = int((X-Y)*((X-Y)+1)/2)
list2[-1] = list2[-1] + L
#print(list1)
#print(list2)
#print(L)
t = ''
if flag == 0:
    for i in range(X):
        t = t + str(list1[i]) + ' '
    for i in range(Y):
        t = t + '-' +str(list2[i]) + ' '
else:
    for i in range(X):
        t = t + '-'+str(list1[i]) + ' '
    for i in range(Y):
        t = t +str(list2[i]) + ' '
print(t)

