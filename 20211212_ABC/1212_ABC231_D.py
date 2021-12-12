import numpy as np

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
#print(l)

mat = np.zeros((n, n))
for i in range(m):
    #print(l[i][0], l[i][1])
    mat[l[i][0]-1, l[i][1]-1] = 1
    mat[l[i][1]-1, l[i][0]-1] = 1
#print(mat)

h, w = l[0][0]-1, l[0][1]-1
while(True):
    #print(h, w)
    flag = 0
    mat[h,w], mat[w,h] = 0, 0
    #print(mat)
    for i in range(n):
        if mat[w, i] == 1:
            h, w = w, i
            flag = 1
    if flag == 0:
        break   

if np.all(mat==0):
    print('Yes')
else:
    print('No')