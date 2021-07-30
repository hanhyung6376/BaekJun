import sys

N, K = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort(reverse=True)

start ,end = 1, max(tree)


while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in tree:
        if i <= mid:
            break
        result += (i - mid)

    if result >= K:
        start = mid +1
    else:
        end = mid - 1

print(end)