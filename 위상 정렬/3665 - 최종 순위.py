import sys
from collections import deque

input = sys.stdin.readline
tc = int(input())
for i in range(tc):
    n = int(input())
    prev_rank = list(map(int, input().split()))
    rank = [[False] * (n+1) for _ in range(n+1)]
    in_degree = [0] * (n+1)

    for j in range(n):
        for l in range(j+1, n):
            rank[prev_rank[j]][prev_rank[l]] = True

    m = int(input())
    for j in range(m):
        a, b = map(int, input().split())

        rank[a][b], rank[b][a] = rank[b][a], rank[a][b]
    final_rank = []

    queue = deque()

    # 진입 차수 계산
    for j in range(1, n+1):
        in_degree[j] = rank[j].count(True)
        if in_degree[j] == 0:
            queue.append(j)

    # 위상 정렬
    while queue:
        cur = queue.popleft()
        final_rank.append(cur)

        for j in range(1, n+1):
            if rank[j][cur]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)

    if len(final_rank) == n:
        print(*final_rank[::-1])
    else:
        print("IMPOSSIBLE")