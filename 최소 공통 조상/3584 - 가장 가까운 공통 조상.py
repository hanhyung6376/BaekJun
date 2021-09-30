import sys

input = sys.stdin.readline

tc = int(input())
for i in range(tc):
    tree_node = int(input())
    tree= [0] * (tree_node + 1)
    for j in range(tree_node - 1):
        parent, child = map(int, input().split())
        tree[child] = parent
    target1, target2 = map(int, input().split())
    target1_parent = [0, target1]
    target2_parent = [0, target2]


    while tree[target1]:
        target1_parent.append(tree[target1])
        target1 = tree[target1]

    while tree[target2]:
        target2_parent.append(tree[target2])
        target2 = tree[target2]

    cnt = 1
    while target1_parent[-cnt] == target2_parent[-cnt]:
        cnt += 1
    print(target1_parent[-cnt + 1])