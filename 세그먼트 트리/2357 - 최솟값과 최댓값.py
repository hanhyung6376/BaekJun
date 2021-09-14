import math
import sys

MAX_VALUE = 1000000001

# 최솟값 트리 초기화
def minInit(node, start, end):
    if start == end:
        min_tree[node] = arr[start]
        return min_tree[node]

    mid = (start + end) // 2
    min_tree[node] = min(minInit(node * 2, start, mid), minInit(node * 2 + 1, mid+1, end))
    return min_tree[node]

# 최댓값 트리 초기화
def maxInit(node, start, end):
    if start == end:
        max_tree[node] = arr[start]
        return max_tree[node]

    mid = (start + end) // 2
    max_tree[node] = max(maxInit(node * 2, start, mid), maxInit(node * 2 + 1, mid + 1, end))
    return max_tree[node]

# 최솟값 쿼리
def minQuery(node, start, end, left, right):
    if start > right or end < left:
        return MAX_VALUE

    if left <= start and end <= right:
        return min_tree[node]

    mid = (start + end) // 2
    return min(minQuery(node * 2, start, mid, left, right), minQuery(node * 2 + 1, mid+1, end, left, right))

# 최댓값 쿼리
def maxQuery(node, start, end, left, right):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return max_tree[node]

    mid = (start + end) // 2
    return max(maxQuery(node * 2, start, mid, left, right), maxQuery(node * 2 + 1, mid+1, end, left, right))

input = sys.stdin.readline
n, m = map(int, input().split())
tree_size = 2 ** math.ceil(math.log2(n))
min_tree, max_tree = [0] * (tree_size * 2), [0] * (tree_size * 2)
arr = []

for i in range(n):
    arr.append(int(input()))

# 트리 초기화
minInit(1, 0, n-1)
maxInit(1, 0, n-1)

for i in range(m):
    a, b = map(int, input().split())

    min_value = minQuery(1, 0, n-1, a-1, b-1)
    max_value = maxQuery(1, 0, n-1, a-1, b-1)
    print(min_value, max_value)
