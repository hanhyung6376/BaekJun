import sys
import heapq

def dijkstra(start):
    dp = [100000000 for i in range(n+1)]
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        now_weight, now = heapq.heappop(heap)

        if dp[now] < now_weight:
            continue
        for next, weight in graph[now]:
            next_weight = now_weight + weight

            if dp[next] > next_weight:
                dp[next] = next_weight
                heapq.heappush(heap, [next_weight, next])
    return dp

input = sys.stdin.readline
inf = float('inf')
tc = int(input())
for i in range(tc):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for i in range(n+1)]
    destinations = []
    result = []
    for j in range(m):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])
        graph[v].append([u, w])
    for j in range(t):
        destinations.append(int(input()))
    first = dijkstra(s)
    second = dijkstra(g)
    third = dijkstra(h)

    for d in destinations:
        if first[d] == first[g] + second[h] + third[d]:
            result.append(d)
        elif first[d] == first[h] + third[g] + second[d]:
            result.append(d)
    result.sort()
    for r in result:
        print(r, end=' ')
    print()
