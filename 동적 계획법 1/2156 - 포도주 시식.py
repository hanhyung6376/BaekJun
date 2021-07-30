import sys

n = int(sys.stdin.readline())
drink = [0] * 10000
dp = [0] * 10000
for i in range(n):
    drink[i] = int(sys.stdin.readline())

dp[0] = drink[0]
dp[1] = drink[0] + drink[1]
dp[2] = max(dp[0] + drink[2], dp[1], drink[1] + drink[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + drink[i], dp[i-1], dp[i-3] + drink[i-1] + drink[i])
print(dp[n-1])