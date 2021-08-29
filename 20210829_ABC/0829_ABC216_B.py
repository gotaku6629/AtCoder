n = int(input())
st = [input().split() for _ in range(n)]
s, t = [list(i) for i in zip(*st)]

flag = 0
for i in range(n-1):
    for j in range(i+1, n):
        if s[i] == s[j] and t[i] == t[j]:
            flag = 1    
if flag == 1:
    print('Yes')
else:
    print('No')