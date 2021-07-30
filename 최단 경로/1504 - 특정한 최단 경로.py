import sys
import heapq

def route(start):
    dijkstra = [INF] * V
    heap = []
    dijkstra[start] = 0 # 시작하는 정점 가중치는 0으로
    heapq.heappush(heap,[0, start]) # 우선순위 큐에 가중치과 시작 정점 삽입

    while heap:
        now_weight, now = heapq.heappop(heap)

        # 현재 테이블과 비교하여 더 가중치가 크다면 무시
        if dijkstra[now] < now_weight:
            continue

        for weight, next in graph[now]:
            next_weight = now_weight + weight # 현재 정점에서 다음 정점까지의 가중치

            if next_weight < dijkstra[next]: # 해당 테이블의 가중치가 현재 정점에서 다음 정점까지의 가중치보다 크다면
                dijkstra[next] = next_weight # 가중치 업데이트
                heapq.heappush(heap, [next_weight, next]) # 우선순위 큐에 삽입
    return dijkstra

V, E = map(int, sys.stdin.readline().split())  # 정점, 간선 입력받기
INF = sys.maxsize
graph = [[] for i in range(V)]

# 간선과 가중치 정보 입력받기
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u-1].append([w, v-1])
    graph[v-1].append([w, u-1])
v1, v2 = map(int, sys.stdin.readline().split())
first = route(0)
seconde = route(v1-1)
third = route(v2-1)
result= min(first[v1-1] + seconde[v2-1] + third[V-1], first[v2-1] + third[v1-1] + seconde[V-1])
print(result if result < INF else -1)