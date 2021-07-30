import sys

dp = [[0 for i in range(10)] for j in range(100)]
for i in range(1, 10):
    dp[0][i] = 1

n = int(sys.stdin.readline())

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j==9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n-1]) % 1000000000)