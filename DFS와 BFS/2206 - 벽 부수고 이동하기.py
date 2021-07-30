import sys
from collections import deque

def BFS():
    if n == 1 and m == 1:
        return 1
    visit = [[[0] * 2 for i in range(m)] for j in range(n)]
    queue = deque()
    queue.append([0, 0, 1])
    visit[0][0][1] = 1
    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx <n) and (0 <= ny < m):
                if matrix[nx][ny] == 1 and z == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    queue.append([nx, ny, 0])
                elif matrix[nx][ny] == 0 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append([nx, ny, z])
    return -1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input())))

print(BFS())