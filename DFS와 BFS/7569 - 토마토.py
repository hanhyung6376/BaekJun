import sys
from collections import deque
def BFS():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if (0 <= nx < n) and (0 <= ny < m) and (0 <= nz < h):
                if matrix[nz][nx][ny] == 0:
                    matrix[nz][nx][ny] = matrix[z][x][y] + 1
                    queue.append([nz, nx, ny])

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, sys.stdin.readline().split())
matrix, queue = [[] for i in range(h)], deque()
result = 0
for i in range(h):
    for j in range(n):
        a = list(map(int, sys.stdin.readline().split()))
        matrix[i].append(a)
for i in range(h):
    for j in range(n):
        for l in range(m):
            if matrix[i][j][l] == 1:
                queue.append([i, j, l])

BFS()

for i in matrix:
    for j in i:
        if 0 in j:
            print(-1)
            result = False
            break
        result = max(result, max(j))
    if not result:
        break
if result:
    print(result-1)