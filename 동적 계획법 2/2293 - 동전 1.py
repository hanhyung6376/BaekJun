import sys

input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0 if i != 0 else 1 for i in range(k+1)]
coin = []
for i in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
print(dp[-1])
