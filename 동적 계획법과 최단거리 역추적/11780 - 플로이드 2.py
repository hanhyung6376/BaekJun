import sys

def floyd_warshall():
    # 경유지
    for k in range(n+1):
        # 출발지
        for i in range(n+1):
            # 도착지
            for j in range(n+1):
                if graph[i][j][0] > graph[i][k][0] + graph[k][j][0]:
                    graph[i][j][0] = graph[i][k][0] + graph[k][j][0]
                    graph[i][j][1] = graph[i][k][1] + graph[k][j][1][1:]

input = sys.stdin.readline
inf = float('inf')
n = int(input())
m = int(input())
graph = [[[inf if i != j else 0, []] for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    v, u, w = map(int, input().split())
    if w < graph[v][u][0]:
        graph[v][u][1] = [v, u]
    elif w >= graph[v][u][0]:
        graph[v][u][1] = graph[v][u][1]
    graph[v][u][0] = min(w, graph[v][u][0])


floyd_warshall()
for i in graph[1:]:
    for j in i[1:]:
        print(j[0] if j[0] != inf else 0, end= ' ')
    print()

for i in graph[1:]:
    for j in i[1:]:
        if j[0] == inf:
            print(0)
            continue
        else:
            print(len(j[1]), end = ' ')
            print(*j[1])