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

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]
isTrue = False

for i in range(m):
    x, y = map(int, input().split())
    # 유니온 연산 전 먼저 둘의 루트 노드 체크 같다면 사이클이 완성됐으므로 break
    if find(x) == find(y):
        isTrue = True
        print(i+1)
        break
    union(x, y)
if not isTrue:
    print(0)
