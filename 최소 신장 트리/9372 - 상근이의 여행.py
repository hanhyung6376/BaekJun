import sys
from collections import deque

def bfs(x):
    queue = deque([x])
    cnt = 0
    while queue:
        now = queue.popleft()
        for i in range(1, n+1):
            if graph[now][i] != 0 and visited[i] == False:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt

input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    graph = [[0 for c in range(n+1)] for r in range(n+1)]
    for j in range(m):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    visited = [False] * (n + 1)
    result = 0
    for j in range(1, n+1):
        if not visited[j]:
            result += bfs(j)
    print(result-1)
