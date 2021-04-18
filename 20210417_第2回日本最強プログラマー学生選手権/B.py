#!/usr/bin/env python
# coding: utf-8

# In[11]:

N, M = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = []
for a in range(N):
    if A[a] not in B:
        S.append(A[a])
for b in range(M):
    if B[b] not in A and B[b] not in S:
        S.append(B[b])
S_sort = sorted(S)

t = ''
for s in range(len(S_sort)):
    t = t + str(S_sort[s]) + ' '
print(t)
