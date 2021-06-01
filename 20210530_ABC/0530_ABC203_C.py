import numpy as np
n, k = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

a_np = np.array(a)
a_ind = np.argsort(a_np)
#print(a_ind)

way = 0
for i in range(n):
    if i == 0:
        if k >= a[a_ind[i]]:
            k =  k - a[a_ind[i]] + b[a_ind[i]]
            if k == 0:
                break
        else:
            way = k        
            break
    else:
        sa = a[a_ind[i]] - a[a_ind[i-1]]
        if k >= sa:
            k =  k - sa + b[a_ind[i]]
            if k == 0:
                break
        else:
            way = a[a_ind[i-1]] + k
            break
        
    if i == n-1:
        way += (a[a_ind[n-1]] + k)    

print(way)

"""
vi = []
for i in range(10**100+1):
    print(i)
    vi.append(0)
#vi = [0 for _ in range(10**100+1)]
print(vi)
for i in range(n):
    vi[a[i]] = b[i]

if k == 0:
    print(0)
else:
    way = 0
    for i in range(1, 10**100+1):
        k -= 1
        if vi[i] != 0:
            k += vi[i]
        if k == 0:
            way = i
            break
print(way)
"""