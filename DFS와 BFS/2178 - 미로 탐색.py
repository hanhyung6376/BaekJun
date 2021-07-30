import sys

def BFS(x, y):
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append([nx, ny])

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())
matrix = []

for i in range(n):
    a = list(map(int, input()))
    matrix.append(a)


BFS(0, 0)
print(matrix[n-1][m-1])