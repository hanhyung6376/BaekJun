import sys
input = sys.stdin.readline

def floyd_whashall():
    # k = 경유지
    for k in range(1, V+1):
        # i = 출발지
        for i in range(1, V+1):
            # j = 목적지
            for j in range(1, V+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


V, E = map(int, input().split())
inf = float('inf')
graph = [[inf for i in range(V+1)] for j in range(V+1)]

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

floyd_whashall()
result = inf

# 사이클은 자신한테 출발해 자신으로 돌아오기 때문에 graph[i][i]
for i in range(1, V+1):
    result = min(result, graph[i][i])

print(result if result != inf else -1)