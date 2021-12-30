
n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
#print(l)

d = {}
f = {}
for i in range(len(l)):
    # その1
    if l[i][0] in d: # もし既に登録されているKeyなら
        d[l[i][0]].append(l[i][1])
    else: # 登録されていない初Keyなら
        d[l[i][0]] = [l[i][1]]
        f[l[i][0]] = False
    # その2
    if l[i][1] in d: # もし既に登録されているKeyなら
        d[l[i][1]].append(l[i][0])
    else: # 登録されていない初Keyなら
        d[l[i][1]] = [l[i][0]]
        f[l[i][1]] = False
#f = [False for _ in range(len(d))]

node = l[0][0]
f[node] = True
while(True):
    #print(node)
    if node in d: # そのKeyがあるなら、
        flag = 0
        for x in d[node]: # 該当するValue（リスト）を見て、
            if not f[x]:  # そのValue（要素）が訪れたことがないなら、
                node = x  # nodeを更新
                f[x] = True
                flag = 1
            if flag == 1:
                break
        if flag == 0: # 一度も更新されなかったら、
            break
    else: # Keyがないなら、
        break
#print(d)
#print(f)

d_flag = True
for i, key in enumerate(f):
    if not f[key]:
        d_flag = False

if d_flag:
    print('Yes')
else:
    print('No')