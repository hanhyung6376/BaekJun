import sys

# 전위순회
def preorder(root):
    if root !='.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위순회
def inorder(root):
    if root !='.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# 후위순회
def postorder(root):
    if root !='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

input = sys.stdin.readline
n = int(input())
tree = {}
for i in range(n):
    root, left, rigth = map(str, input().split())
    tree[root] = [left, rigth]

preorder('A')
print()
inorder('A')
print()
postorder('A')