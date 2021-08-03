import sys

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        number[a] += number[b]


def find(target):
    if target == parent[target]:
        return target

    # 경로 압축
    parent[target] = find(parent[target])
    return parent[target]

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
tc = int(input())

for i in range(tc):
    f = int(input())
    parent = {}
    number = {}
    for j in range(f):
        f1, f2 = map(str, input().split())
        if f1 not in parent:
            parent[f1] = f1
            number[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            number[f2] = 1
        union(f1, f2)
        print(number[find(f1)])
