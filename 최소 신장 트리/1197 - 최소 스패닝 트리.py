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

V, E = map(int, input().split())
graph = []
parent = [i for i in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph.append([u, v, w])
graph.sort(key = lambda x: x[2])

print(kruskal())
