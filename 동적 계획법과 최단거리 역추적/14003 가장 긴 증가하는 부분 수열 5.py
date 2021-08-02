import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
numbers = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
cmp = [-1000000001] # 현재 인덱스 저장
maxvalue = 0


for i in range(1, n+1):
    if cmp[-1] < numbers[i]:
        cmp.append(numbers[i])
        dp[i] = len(cmp) - 1
        maxvalue = dp[i]
    else:
        dp[i] = bisect_left(cmp, numbers[i])
        cmp[dp[i]] = numbers[i]
print(maxvalue)

result = []
for i in range(n, 0, -1):
    if dp[i] == maxvalue:
        result.append(numbers[i])
        maxvalue -= 1
result.reverse()
print(*result)