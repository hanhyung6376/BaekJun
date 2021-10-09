import sys

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False and i != 0:
            dfs(i)
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] for i in range(n+1)]
visited = [False] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        answer += 1
print(answer)