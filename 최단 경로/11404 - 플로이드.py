import sys

def floyd_warshall():
    # k = 거쳐가는 노드
    for k in range(1, n+1):
        # i = 출발하는 노드
        for i in range(1, n+1):
            # j = 도착하는 노드
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

INF = float('inf')
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[0 if i==j else INF for i in range(n+1)] for j in range(n+1)]

for i in range(m):
    v, u, w = map(int, input().split())
    graph[v][u] = min(w, graph[v][u])

floyd_warshall()

for i in graph[1:]:
    for j in i[1:]:
        print(0 if j==INF else j, end=' ')
    print()