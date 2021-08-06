import sys
from collections import deque
def bfs():
    queue=deque()
    result = []

    for i in range(1, n+1):
        if degree[i] == 0:
            queue.append(i)

    while queue:
        student = queue.popleft()

        for i in graph[student]:
            degree[i] -= 1
            if degree[i] == 0:
                queue.append(i)
        result.append(student)
    return result



input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
degree = [0 for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

print(*bfs())