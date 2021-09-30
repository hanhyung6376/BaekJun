from collections import deque
import sys


def bfs(start):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                queue.append(next)
    answer = []
    for i in range(n+1):
        if visited[i] == k:
            answer.append(i)
    answer.sort()
    return answer

input = sys.stdin.readline
inf = float('inf')

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [-1] * (n+1)
visited[x] = 0
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = bfs(x)
if result:
    for i in result:
        print(i)
else:
    print(-1)