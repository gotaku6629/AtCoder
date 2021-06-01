n, k = map(int, input().split())

sum = 0
for i in range(n):
    for j in range(k):
        sum += 100*(i+1)+(j+1)
print(sum)