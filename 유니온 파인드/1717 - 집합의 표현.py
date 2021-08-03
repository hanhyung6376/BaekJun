import sys

# 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 찾기
def find(target):
    if target == parent[target]:
        return target

    # 경로 압축
    parent[target] = find(parent[target])
    return parent[target]


input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for i in range(m):
    op, a, b = map(int, input().split())
    # 유니온 연산
    if op == 0:
        union(a, b)
    # 파인드 연산
    elif op == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')