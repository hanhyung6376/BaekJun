import sys

def dfs(x):
    count[x] = 1
    for i in tree[x]:
        if not count[i]:
            dfs(i)
            count[x] += count[i]

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n, r, q = map(int, input().split())

tree = [[] for i in range(n+1)]
count = [0] * (n+1)

for i in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(r)

for i in range(q):
    query = int(input())
    print(count[query])