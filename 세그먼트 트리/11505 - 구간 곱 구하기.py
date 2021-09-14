import math
import sys

MOD = 1000000007
# start, end => 전체 구간, left, right => 탐색 구간, node => 트리에서의 위치


def tree_mul(node, start, end, left, right):
    # 찾는 구간이 아니면
    if right < start or end < left:
        return 1

    # 찾는 구간이라면 노드값 반환
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    # 왼쪽, 오른쪽 나누어서 재귀
    return tree_mul(node * 2, start, mid, left, right) * tree_mul(node * 2 + 1, mid + 1, end, left, right) % MOD

# 트리 값 업데이트
def update(node, start, end, idx, value):
    # 범위를 벗어날 경우
    if idx < start or  end < idx:
        return

    # 리프 노드
    if start == end:
        tree[node] = value
        return

    mid = (start + end) // 2
    # 연관된 노드 변경
    update(node*2, start, mid, idx, value)
    update(node * 2 + 1, mid + 1, end, idx, value)
    tree[node] = (tree[node * 2] * tree[node * 2 +1]) % MOD

input = sys.stdin.readline
n, m, k = map(int, input().split())
tree_size = math.ceil(math.log2(n))
tree_size = 1 << (tree_size+1)
tree = [0] *  tree_size



for i in range(n):
    num = int(input())
    update(1, 0, n-1, i, num)

for i in range(m+k):
    a, b, c = map(int, input().split())
    if a==1:
        update(1, 0, n-1, b-1, c)
    else:
        print(tree_mul(1, 0, n-1, b-1, c-1))
