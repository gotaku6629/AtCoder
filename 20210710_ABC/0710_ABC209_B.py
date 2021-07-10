n, x = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
for i in range(n):
    if i%2 == 1:
        a[i] = a[i]-1
    sum = sum + a[i]

if x >= sum:
    print('Yes')
else:
    print('No')