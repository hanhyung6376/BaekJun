import sys
from collections import deque

def bfs(start):
    queue = deque()
    visited = [-1] * (n+1)
    queue.append(start)
    visited[start] = 0
    value =  [0, 0]
    while queue:
        now = queue.popleft()
        for next, dist in tree[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + dist
                queue.append(next)
                if value[0] < visited[next]:
                    value = visited[next], next
    return value

input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    v, u, w = map(int, input().split())
    tree[v].append([u, w])
    tree[u].append([v, w])


distance, node = bfs(1)
distance, node = bfs(node)
print(distance)