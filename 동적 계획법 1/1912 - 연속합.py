import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [arr[0]]

for i in range(n-1):
    dp.append(max(dp[i] + arr[i+1], arr[i+1]))

print(max(dp))
