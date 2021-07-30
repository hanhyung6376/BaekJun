import sys

def bellmanFord(start):
    dp = [INF] * (N + 1)
    dp[start] = 0

    for i in range(N-1):
        for j in range(1, N+1):
            for next, weight in graph[j]:
                if dp[next] > dp[j] + weight:
                    dp[next] = dp[j] + weight

    for i in range(1, N+1):
        for node, weight in graph[i]:
            if dp[node] > dp[i] + weight:
                return False
    return dp

N, M = map(int, sys.stdin.readline().split())
INF = float('inf')
graph = [[] for i in range(N+1)]

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append([B, C])

result = bellmanFord(1)
if result == False:
    print(-1)
else:
    for i in result[2:]:
        print(i if i < INF else -1)