n, k = map(int, input().split())
c = list(map(int, input().split()))

#m = 10**9
m = max(c)
#bp = [0 for _ in range(m)]
bp = [0] * m

max = 0
for i in range(k):
    bp[c[i]-1] += 1
    if bp[c[i]-1] == 1:
        max += 1

count = max
for i in range(n-k):
    bp[c[i]-1] -= 1
    if bp[c[i]-1] == 0:
        count -= 1

    if bp[c[k+i]-1] == 0:
        count += 1
    bp[c[k+i]-1] += 1

    if count > max:
        max = count
print(max)