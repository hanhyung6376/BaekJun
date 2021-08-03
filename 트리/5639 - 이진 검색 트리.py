import sys
from collections import deque

def order(start, end):
    if start > end:
        return
    root = tree[start]
    preorder.appendleft(root) # left, right, root 순이므로 appendleft를 이용한다.

    idx = start + 1
    while idx <= end:
        if tree[idx] > root:
            break
        idx += 1

    order(idx, end)   #오른쪽 노드
    order(start+1, idx-1) # 왼쪽 노드

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
preorder = deque()
tree = []
count = 0
while count <= 10000:
    try:
        temp = int(input())
    except:
        break
    tree.append(temp)
    count += 1

order(0, len(tree)-1)
print(*preorder)