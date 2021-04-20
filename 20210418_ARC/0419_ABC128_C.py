#!/usr/bin/env python
# coding: utf-8

# In[18]:


N, M = map(int, input().split())
kS = [list(map(int, input().split())) for l in range(M)]
P = list(map(int, input().split()))

#switch = [0 for i in range(N)]
count = 0
# スイッチのbit全探索
for i in range(2**N):
    light = [0 for _ in range(M)]
    flag = 0
    for j in range(N): # 現状のbit列で, 1の要素を順番に見ていく!
        if ((i >> j) & 1): # j番目の要素が1なら...
            for m in range(M): # 電球の数
                for k in range(kS[m][0]): # m番目の電球の全スイッチの数
                    if j+1 == kS[m][k+1]: # もし含まれていたら...
                        light[m] = light[m] + 1
    
    for v in range(M):
        if light[v] % 2 != P[v]:
            flag = 1
            break
    if flag != 1:
        count += 1
print(count)
                


# In[ ]:




