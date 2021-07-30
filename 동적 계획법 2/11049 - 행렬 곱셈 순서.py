import sys

input = sys.stdin.readline

n = int(input())
matrix = []
dp = [[0 for i in range(n)] for j in range(n)]
max_size = 2 ** 32
for i in range(n):
    matrix.append(list(map(int, input().split())))


for i in range(1, n):
    for j in range(n-i):
        x = i+j
        dp[j][x] = max_size
        for k in range(j, x):
            matrix_mul = matrix[j][0] * matrix[k][1] * matrix[x][1] # 행렬 곱셈의 횟수
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + matrix_mul)
print(dp[0][n-1])