import sys


# 유니온 (집합 합치기)
def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 파인드 (루트 노드 찾기)
def find(target):
    if target == parent[target]:
        return target

    parent[target] = find(parent[target])
    return parent[target]


input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())
m = int(input())
parent = [i for i in range(n)]
isTrue = True
for i in range(n):
    check = list(map(int, input().split()))
    # union 연산
    for c in range(len(check)):
        if check[c] == 1:
            union(i, c)

plan = list(map(int, input().split()))

# find 연산
for i in range(1, len(plan)):
    if find(plan[i - 1] - 1) != find(plan[i] - 1):
        isTrue = False
        break

print('YES' if isTrue else 'NO')