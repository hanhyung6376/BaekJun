def DFS(idx, network, visited):
    global answer
    visited[idx] = True
    answer += 1
    for i in range(n):
        if visited[i] == False and network[idx][i] == 1:
            DFS(i, network, visited)


n =  int(input())
m = int(input())
network = [[0 for i in range(n)] for j in range(n)]
visited = [False] * n
for i in range(m):
    x, y = map(int, input().split())

    network[x-1][y-1] = 1
    network[y-1][x-1] = 1
answer = 0
DFS(0, network, visited)
print(answer-1)