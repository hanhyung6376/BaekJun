import sys

def dfs(x, y):
    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<= nx < h) and (0 <= ny < w):
             if (visited[nx][ny] == False) and (graph[nx][ny] == 1):
                 dfs(nx, ny)


dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
while 1:
    w, h = map(int, input().split())
    graph = []
    visited = [[False for i in range(w)] for j in range(h)]
    count = 0
    if (w == 0 and h == 0):
        break
    for i in range(h):
        geo = list(map(int, input().split()))
        graph.append(geo)
    for i in range(h):
        for j in range(w):
            if graph[i][j] and visited[i][j] == False:
                dfs(i, j)
                count += 1
    print(count)