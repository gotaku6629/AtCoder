n = int(input())
h = list(map(int, input().split()))

max = h[0]
for i in range(1, len(h)):
    if max < h[i]:
        max = h[i]
    else:
        break
print(max)