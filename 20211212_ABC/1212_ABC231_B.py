n = int(input())
s = []
for i in range(n):
    s.append(input())

dic = {}
for si in s:
    if si not in dic:
        dic[si] = 1
    else:
        dic[si] += 1
#print(dic)
id = 0
max = 0
for i, k in enumerate(dic):
    #print(dic[k])
    if max < dic[k]:
        max = dic[k]
        id = i

for i, k in enumerate(dic):
    if id == i:
        print(k)