import sys

def dfs(start):
    visited[start] = True
    dp[start][0] = weight[start]
    num[start][0].append(start)

    for i in tree[start]:
       if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            for j in num[i][1]:
                num[start][0].append(j)
            if dp[i][0] <= dp[i][1]:
                dp[start][1] += dp[i][1]
                for j in num[i][1]:
                    num[start][1].append(j)
            else:
                dp[start][1] += dp[i][0]
                for j in num[i][0]:
                    num[start][1].append(j)


input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())
weight = [0] + list(map(int, input().split()))
tree = [[] for i in range(n+1)]
visited = [False] * (n+1)
num = [[[], []] for i in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for i in range(n+1)]

dfs(1)

if dp[1][0] >= dp[1][1]:
    print(dp[1][0])
    num[1][0].sort()
    print(*num[1][0])
else:
    print(dp[1][1])
    num[1][1].sort()
    print(*num[1][1])
