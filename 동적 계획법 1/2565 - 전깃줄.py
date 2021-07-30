import sys

n = int(sys.stdin.readline())
wire = []
dp= [0] * n

for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    wire.append([A, B])

wire = sorted(wire, key = lambda x: x[0])

for i in range(n):
    for j in range(i):
        if wire[i][1] > wire[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))