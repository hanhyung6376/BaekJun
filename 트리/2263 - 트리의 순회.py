import sys

def order(in_left, in_right, post_left, post_right):
    if(in_left > in_right) or (post_left > post_right):
        return

    root = postorder[post_right]
    preorder.append(root)

    left = location[root] - in_left
    right = in_right - location[root]

    order(in_left, in_left + left -1, post_left, post_left + left - 1) # 왼쪽 노드
    order(in_right - right + 1, in_right, post_right - right, post_right - 1) # 오른쪽 노드

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
preorder = []
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
location = [0] * (n+1)
for i in range(n):
    location[inorder[i]] = i
order(0, n-1, 0, n-1)
print(*preorder)
