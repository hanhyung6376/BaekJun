import sys


def BFS(y, x):
    queue = [[y, x]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            ny = a+dx[i]
            nx = b+dy[i]
            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 1:
                matrix[ny][nx] = 0
                queue.append([ny, nx])

tc = int(sys.stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(tc):
    M, N, K = map(int, sys.stdin.readline().split())
    matrix = [[0 for i in range(M)] for j in range(N)]
    cnt = 0
    for j in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        matrix[Y][X] = 1

    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1:
                BFS(y, x)
                matrix[y][x] = 0
                cnt +=1
    print(cnt)
