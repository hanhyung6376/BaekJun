import sys
import heapq

def BFS():
    global dp
    queue = []
    heapq.heappush(queue, [-matrix[0][0], 0, 0])
    dp[0][0] = 1
    while queue:
        num, x, y = heapq.heappop(queue)
        num = -1 * num
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] < num:
                    if dp[nx][ny] == 0:
                        heapq.heappush(queue, [-matrix[nx][ny], nx, ny])
                    dp[nx][ny] += dp[x][y]


input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
dp = [[0 for i in range(m)] for j in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    matrix.append(list(map(int, input().split())))

BFS()
print(dp[n-1][m-1])