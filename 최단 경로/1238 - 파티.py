# 다익스트라
import sys
import heapq

def dijkstra(start):
    heap = []
    dp = [inf] * (n + 1)
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        now_weight, now = heapq.heappop(heap)
        if dp[now] < now_weight:
            continue

        for next, cost in graph[now]:
            next_weight = now_weight + cost

            if next_weight < dp[next]:
                dp[next] = next_weight
                heapq.heappush(heap, (next_weight, next))
    return dp


input = sys.stdin.readline
inf = float('inf')

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

answer = 0

for i in range(1, n+1):
    answer = max(answer, dijkstra(i)[x] + dijkstra(x)[i])

print(answer)