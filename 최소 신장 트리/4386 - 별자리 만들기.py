import sys
import math


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
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# 크루스칼 알고리즘
def kruskal():
    tree_edges = 0
    cost = 0
    for u, v, w in graph:
        # 루트 노드가 같지 않다면 두 노드를 합치고 가중치를 더함
        if find(u) != find(v):
            union(u, v)
            cost += w
    return cost


input = sys.stdin.readline

n = int(input())
point = []
for i in range(n):
    x, y = map(float, input().split())
    point.append([x, y])
graph = []

# 그래프 만들기
for i in range(len(point)):
    for j in range(i + 1, len(point)):
        graph.append([i, j, distance(point[i], point[j])])

parent = [i for i in range(len(graph))]

graph.sort(key=lambda x: x[2])

print(round(kruskal(), 2))