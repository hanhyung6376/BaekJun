import sys
from collections import deque

def bfs(n):
    visited[n] = 1;
    queue=deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        for i in matrix[x]:
            if visited[i] == 0:
                visited[i] = -visited[x]
                queue.append(i)
            else:
                if visited[i] == visited[x]:
                    return False
    return True



tc = int(sys.stdin.readline())

for i in range(tc):
    v, e = map(int, sys.stdin.readline().split())
    x, y = [], []
    visited = [0] * (v+1)
    matrix = [[] for r in range(v+1)]
    for j in range(e):
        x, y = map(int, sys.stdin.readline().split())
        matrix[x].append(y)
        matrix[y].append(x)

    result = 'YES'
    for j in range(1, v+1):
        if visited[j] == 0:
            if not bfs(j):
                result = 'NO'
                break
    print(result)