import sys

A = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
dp = [0] * A
for i in range(A):
    for j in range(i):
        if seq[i] > seq[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))