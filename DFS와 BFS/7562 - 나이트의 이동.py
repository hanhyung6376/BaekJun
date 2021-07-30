import sys
from collections import deque

def BFS(matrix, start, end):
    if start == end:
        return 1
    queue = deque()
    queue.append([start[0], start[1]])
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < height:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append([nx, ny])
                    if nx == end[0] and ny == end[1]:
                        return matrix[nx][ny]

dx = [2, 1, 2, 1, -2, -1, -2, -1]
dy = [1, 2, -1, -2, 1, 2, -1, -2]

tc = int(sys.stdin.readline())
for i in range(tc):
    height = int(sys.stdin.readline())
    matrix = [[0 for i in range(height)] for j in range(height)]
    start = list(map(int, sys.stdin.readline().split()))
    matrix[start[0]][start[1]] = 1
    end = list(map(int, sys.stdin.readline().split()))
    print(BFS(matrix, start, end) - 1)