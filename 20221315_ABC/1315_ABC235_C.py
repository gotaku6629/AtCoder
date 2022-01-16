n, q = map(int, input().split())
a = list(map(int, input().split()))

xk = [map(int, input().split()) for _ in range(q)]
x, k = [list(i) for i in zip(*xk)]

# 辞書リスト
d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = [i]
    else:
        d[a[i]].append(i)
#print(d)

# クエリー探索
for i in range(q): # 2*10**5
    xi, ki = x[i], k[i]
    if xi not in d:
        print('-1')
    else: # keyはあって、
        if ki > len(d[xi]): # 超えていたら
            print('-1')
        else: # ki > len(d[xi]):
            print(d[xi][ki-1]+1)