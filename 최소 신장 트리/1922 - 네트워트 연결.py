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

def kruskal():
    cost = 0
    for u, v, w in graph:
        if find(u) != find(v):
            union(u, v)
            cost += w
    return cost


input = sys.stdin.readline

n = int(input())
m = int(input())
graph = []
parent = [i for i in range(n+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph.append([u, v, w])
graph.sort(key =  lambda x: x[2])

print(kruskal())