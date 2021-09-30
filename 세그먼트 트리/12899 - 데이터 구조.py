import sys
import math


def update(num):
    while num >= 1:
        tree[num] += 1
        num//= 2


def tree_remove(node, num):
    while node < tree_size:
        if tree[node*2] < num:
            num -=  tree[node*2]
            node = node*2+1
        else:
            node = node *2
    return node
input = sys.stdin.readline

MAZ_SIZE = 2000000
tree_size = 2 ** math.ceil(math.log2(MAZ_SIZE))
tree= [0] * (2*tree_size)
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == 1:
        update(tree_size+b-1)
    else:
        temp = tree_remove(1, b)
        print(temp-tree_size+1)
        while temp >= 1:
            tree[temp] -= 1
            temp //= 2