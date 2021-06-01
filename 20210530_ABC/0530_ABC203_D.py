n, k = map(int, input().split())
a = [list(map(int, input().split())) for l in range(n)]

mid_ind = int((k**2)/2) + 1
mid_list = []
for i in range(n-k+1):
    for j in range(n-k+1):
        x = []
        for h in range(k):
            for w in range(k):
                x.append(a[h+i][w+j])
        x.sort()
        #print(x)
        mid_list.append(x[-mid_ind])
#print(mid_list)
print(min(mid_list))