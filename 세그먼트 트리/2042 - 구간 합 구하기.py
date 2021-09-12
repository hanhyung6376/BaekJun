import math
import sys

# DP로 리프노드가 아닌 노드들 전처리
def init():
    for i in range(tree_size-1, 0, -1):
        tree[i] = tree[i*2] + tree[i*2+1]

# start, end => 전체 구간, left, right => 탐색 구간, node => 트리에서의 위치
def tree_sum(start, end, left, right, node):
    # 찾는 구간이 아니면
    if right < start or end < left:
        return 0

    # 찾는 구간이라면 노드값 반환
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    # 왼쪽, 오른쪽 나누어서 재귀
    return tree_sum(start, mid, left, right, node * 2) + tree_sum(mid+1, end, left, right, node * 2 + 1)

# 트리 값 업데이트
def update(index, diff):
    temp = index + tree_size - 1
    while temp >= 1:
        tree[temp] += diff
        temp //= 2

input = sys.stdin.readline
n, m, k = map(int, input().split())
tree_size = 2 ** math.ceil(math.log2(n))
tree = [0] * (tree_size * 2)

for i in range(n):
    tree[tree_size+i] = int(input())

init()

for i in range(m+k):
    a, b, c = map(int, input().split())
    if a==1:
        diff = c - tree[tree_size+b-1]
        update(b, diff)
    else:
        print(tree_sum(1, tree_size, b, c, 1))
