s = input()
t = 'chokudai'
mod = 10**9+7
print(mod)
#s = 'abbcaabc'
#t = 'abc'
h = len(t)  # 番兵(padding)の追加
w = len(s)
dp = [[0] * (w+1) for _ in range(h+1)] # [h+1, w+1]
#print(dp)

for j in range(w+1):
    dp[0][j] = 1
#print(dp)
for i in range(h):
    for j in range(w):
        if t[i] == s[j]:
            dp[i+1][j+1] = (dp[i+1][j] + dp[i][j]) % mod
        else:
            dp[i+1][j+1] = dp[i+1][j]
print(dp[h][w])
