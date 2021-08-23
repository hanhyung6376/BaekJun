
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = numbers[i]
    else:
        dp[i] = dp[i-1] + numbers[i]

for i in range(m):
    p1, p2 = map(int, input().split())
    if p1 == 1:
        print(dp[p2-1])
    else:
        print(dp[p2-1] - dp[p1-2])