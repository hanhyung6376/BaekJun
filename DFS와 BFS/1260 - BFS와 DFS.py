def dfs_solution(graph, v, visited, n):
    visited[v] = True
    dfs_list.append(v + 1)
    for i in range(0, n):
        if visited[i] == False and graph[v][i] == 1:
            dfs_solution(graph, i, visited, n)

def bfs_solution(graph, v, visited, n):
    queue = [v]
    visited[v] = True
    while queue:
        v = queue.pop(0)
        bfs_list.append(v+1)
        for i in range(0, n):
            if visited[i] == False and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[0 for i in range(n)] for j in range(n)]
dfs_visited = [False] * n
bfs_visited = [False] * n
dfs_list = []
bfs_list = []
for i in range(m):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

dfs_solution(graph, v-1, dfs_visited, n)
for i in dfs_list:
    print(i, end=' ')
print()
bfs_solution(graph, v-1, bfs_visited, n)
for i in bfs_list:
    print(i , end=' ')