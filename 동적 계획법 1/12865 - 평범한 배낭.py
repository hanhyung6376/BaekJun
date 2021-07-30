import sys

n, k = map(int, sys.stdin.readline().split())
wv = []
dp = [[0 for i in range(k+1)] for j in range(n+1)]

for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    wv.append([w, v])

for i in range(1,n+1):
    for j in range(1, k+1):
        w = wv[i-1][0]
        v = wv[i-1][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[n][k])