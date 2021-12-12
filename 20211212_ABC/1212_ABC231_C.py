import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]

a.sort()
#print(a)
for xi in x:
    print(n-bisect.bisect_left(a, xi))


