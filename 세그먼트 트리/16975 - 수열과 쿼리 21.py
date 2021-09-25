import sys
import math

# 트리 업데이트
def update(start, end, left, right, node, diff):
    if right < start or left > end:
        return
    if left <= start and end <= right:
        tree[node] += diff
        return
    mid = (start + end) // 2
    update(start, mid, left, right, 2*node, diff)
    update(mid+1, end, left, right, 2*node+1, diff)

# target 노드 찾기
def find(node):
    global answer
    while node >= 1:
        answer += tree[node]
        node = node // 2

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tree_size = 2 ** math.ceil(math.log2(n))
tree = [0] * (tree_size * 2)
for i in range(n):
    tree[tree_size + i] = arr[i]

m = int(input())
for i in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        update(1, tree_size, query[1], query[2], 1, query[3])
    else:
        answer = 0
        find(tree_size+query[1]-1)
        print(answer)


