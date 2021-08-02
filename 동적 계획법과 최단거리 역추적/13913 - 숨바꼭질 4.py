import sys
from collections import deque

def path(x):
    arr = []
    temp = x
    for i in range(matrix[x] + 1):
        arr.append(temp)
        temp = move[temp]
    arr.reverse()
    print(*arr)

def BFS(n):
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        for i in range(3):
            if dx[i] == 2:
                nx = x *2
            else:
                nx = x + dx[i]

            if (0 <= nx < idx):
                if matrix[nx] == 0:
                    matrix[nx] = matrix[x] + 1
                    move[nx] = x
                    if nx == k:
                        print(matrix[k])
                        path(nx)
                        return
                    queue.append(nx)

dx = [1, -1, 2]

input = sys.stdin.readline
n, k = map(int, input().split())
idx = 200000
matrix = [0] * idx
move = [0] * idx

if n == k:
    print(0)
    print(n)
else:
    BFS(n)