import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dp = [[0, []] for i in range(n)]
dp[0][0] = 0

for i in range(n):
    dp[i][1].append(numbers[i])
    for j in range(i):
        if numbers[i] > numbers[j] and dp[i][0] < dp[j][0]:
            dp[i][0] = dp[j][0]
            dp[i][1] = dp[j][1] + [numbers[i]]
    dp[i][0] += 1
dp.sort(key = lambda x: x[0])
print(dp[-1][0])
for i in dp[-1][1]:
    print(i, end=' ')