import sys
import heapq
def dijkstra(start):
    dp[start][0] = 0
    dp[start][1] = [start]
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        now_weigth, now = heapq.heappop(heap)

        if dp[now][0] < now_weigth:
            continue

        for next, weight in graph[now]:
            next_weight = weight + now_weigth

            if next_weight < dp[next][0]:
                dp[next][0] = next_weight
                dp[next][1] = dp[now][1] + [next]
                heapq.heappush(heap, [next_weight, next])

input = sys.stdin.readline
inf = float('inf')
n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
dp = [[inf, []] for i in range(n+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
start, end = map(int, input().split())
dijkstra(start)
print(dp[end][0])
print(len(dp[end][1]))
print(*dp[end][1])