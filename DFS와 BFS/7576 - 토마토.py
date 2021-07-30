import sys
from collections import deque
def BFS():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append([nx, ny])


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
m, n = map(int, sys.stdin.readline().split())
matrix, queue = [], deque()
result = 0
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    matrix.append(a)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

BFS()

for i in matrix:
    if 0 in i:
        print(-1)
        result = False
        break
    result = max(result, max(i))

if result:
    print(result-1)