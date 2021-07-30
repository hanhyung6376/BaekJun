import sys

input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
dp = [[0 for i in range(sum(cost) + 1)] for j in range(N+1)]
result = sum(cost)


for i in range(1, N+1):
    m = memory[i-1]
    c = cost[i-1]

    for j in range(1, sum(cost) + 1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(m + dp[i-1][j-c], dp[i-1][j])

        if dp[i][j] >= M:
            result = min(result, j)
print(result if M != 0 else 0)
