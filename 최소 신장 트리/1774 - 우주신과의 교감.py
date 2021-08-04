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
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

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

n, m = map(int, input().split())
point = []
old_point = []
parent = [i for i in range(n)]
graph =[]
for i in range(n):
    x, y = map(int, input().split())
    point.append([x, y])

# 이미 연결된 점은 미리 union
for i in range(m):
    x, y = map(int, input().split())
    union(x-1, y-1)

# 그래프 만들기
for i in range(len(point)):
    for j in range(i+1, len(point)):
        graph.append([i, j, distance(point[i], point[j])])

graph.sort(key = lambda x: x[2])

print('%.2f' %(kruskal()))
