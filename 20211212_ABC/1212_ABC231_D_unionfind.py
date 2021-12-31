from UnionFind import UnionFind

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]

d = [0 for _ in range(n)]
uf = UnionFind(n)

for i in range(m):
    a, b = l[i][0], l[i][1]
    a -= 1
    b -= 1
    if uf.same(a, b):
        print('No')
        break
    uf.unite(a, b)
    d[a] += 1
    d[b] += 1

for i in range(n):
    if d[i] > 2:
        print('No')

"""
n = 5
uf = UnionFind(n)
uf.unite(1, 2)
#uf.unite(4, 3) # (葉, 根)
#uf.unite(4, 5)
uf.unite(3, 4)
uf.unite(5, 4)

print(uf.find(1)) # 2
print(uf.find(2)) # 2
print(uf.find(3)) # 3
print(uf.find(4)) # 3
print(uf.find(5)) # 3

print(uf.same(1, 2)) # True
print(uf.same(1, 3)) # False
"""