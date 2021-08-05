import sys

def dfs(start):
    visited[start] = True
    dp[start][0] = 0
    dp[start][1] = 1

    for i in tree[start]:
       if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += min(dp[i][0], dp[i][1])


input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())
tree = [[] for i in range(n+1)]
visited = [False] * (n+1)
for i in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for i in range(n+1)]

dfs(1)
print(min(dp[1][0], dp[1][1]))