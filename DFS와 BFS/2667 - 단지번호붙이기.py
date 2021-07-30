import sys

def dfs(x, y, c):
    visited[x][y] = True
    global apart_cnt

    if matrix[x][y]:
        apart_cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <N and 0 <= ny < N:
            if visited[nx][ny] == False and matrix[nx][ny] == 1:
                dfs(nx, ny, c)

N = int(sys.stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False for i in range(N)] for j in range(N)]
matrix = []
for i in range(N):
    n = sys.stdin.readline().strip()
    n = list(n)
    n = [int(j) for j in n]
    matrix.append(n)

cnt = 1
apart_list = []
apart_cnt = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j]  and visited[i][j] == 0:
            dfs(i, j, cnt)
            apart_list.append(apart_cnt)
            apart_cnt = 0
print(len(apart_list))
for n in sorted(apart_list):
    print(n)