import sys
from collections import deque
def BFS(n):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        for i in range(3):
            if dx[i] == 2:
                nx = x * 2
            else:
                nx = x + dx[i]

            if (0<= nx <idx):
                if matrix[nx] == 0:
                    matrix[nx] = matrix[x] + 1
                    if nx == k:
                        return
                    queue.append(nx)


dx = [1, -1, 2]

n, k = map(int, sys.stdin.readline().split())
idx = 200000
matrix = [0] * idx
matrix[n] = 1
if n == k:
    print(0)
else:
    BFS(n)
    print(matrix[k]-1)