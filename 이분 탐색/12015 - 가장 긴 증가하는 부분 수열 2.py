import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = []

for i in arr:
    k = bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i
print(len(dp))