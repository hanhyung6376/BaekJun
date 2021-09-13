import sys

def dfs(x, visited):
    # 도시를 모두 순환했을 때
    if visited == (1 << (n-1)) -1:
        if matrix[x][0]:
            return matrix[x][0]
        else:
            return inf
    if dp[x][visited] != -1:
        return dp[x][visited]
    dp[x][visited] = inf
    for i in range(1, n):
        # x 에서 i로 가는 경로가 없을 경우
        if not matrix[x][i]:
            continue
        # i에 이미 방문했을 경우
        if visited & ( 1 << i -1 ):
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << (i-1))) + matrix[x][i])
    return dp[x][visited]

input = sys.stdin.readline
inf = float('inf')
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
dp = [[-1] * (1 << n) for i in range(n)]

print(dfs(0, 0))