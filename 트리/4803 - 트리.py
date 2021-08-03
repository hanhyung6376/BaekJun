import sys
from collections import deque

def bfs(x):
    isTree = True
    queue = deque([x])
    while queue:
        now = queue.popleft()
        if visited[now] == 1: # 현재 정점을 다른 요소가 방문했다면(사이클을 이루므로 트리가 아님)
            isTree = False
        visited[now] = 1
        for j in tree[now]:
            if visited[j] == 0:
                queue.append(j)
    return isTree



input = sys.stdin.readline
case = 0
while True:
    case += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    tree = [[] for i in range(n+1)]
    visited = [0] * (n+1)
    count = 0
    for i in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    for i in range(1, n+1):
        if visited[i]:
            continue
        if bfs(i):
            count += 1
    if count == 0:
        print(f'Case {case}: No trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {count} trees.')