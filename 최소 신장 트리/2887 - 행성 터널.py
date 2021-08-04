import sys

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(target):
    if target == parent[target]:
        return target

    parent[target] = find(parent[target])
    return parent[target]

# 거리 계산
def distance(a, b):
    return min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))

# 크루스칼 알고리즘
def kruskal():
    cost = 0
    for u, v, w in graph:
        # 루트 노드가 같지 않다면 두 노드를 합치고 가중치를 더함
        if find(u) != find(v):
            union(u, v)
            cost += w
    return cost

input = sys.stdin.readline

n = int(input())
x_point, y_point, z_point = [], [], []
parent = [i for i in range(n)]

graph =[]
for i in range(n):
    x, y, z = map(int, input().split())
    x_point.append([x, i])
    y_point.append([y, i])
    z_point.append([z, i])
x_point.sort()
y_point.sort()
z_point.sort()
for i in range(1, n):
    graph.append([x_point[i][1], x_point[i-1][1], abs(x_point[i][0] - x_point[i-1][0])])
    graph.append([y_point[i][1], y_point[i - 1][1], abs(y_point[i][0] - y_point[i - 1][0])])
    graph.append([z_point[i][1], z_point[i - 1][1], abs(z_point[i][0] - z_point[i - 1][0])])

graph.sort(key = lambda x: x[2])

print(kruskal())
