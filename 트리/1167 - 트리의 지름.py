import sys
from collections import deque

def bfs(start):
    queue = deque()
    visited = [-1] * (V+1)
    queue.append(start)
    visited[start] = 0
    value =  [0, 0]
    while queue:
        now = queue.popleft()
        for next, dist in graph[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + dist
                queue.append(next)
                if value[0] < visited[next]:
                    value = visited[next], next
    return value

input = sys.stdin.readline
inf = float('inf')
V = int(input())
tree = []
graph = [[] for j in range(V+1)]
for i in range(V):
    tree.append(list(map (int, input().split())))

for i in tree:
    for j in range(1, len(i), 2):
        if i[j] == -1:
            break
        graph[i[0]].append([i[j], i[j+1]])

distance, node = bfs(1)
distance, node = bfs(node)
print(distance)
