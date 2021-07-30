import sys
from collections import deque
def BFS():
    answer = [0] * n
    visited = [False] * (n+1)
    queue = deque([1])
    while queue:
        parent = queue.popleft()

        for i in tree[parent]:
            if not visited[i]:
                answer[i-1] = parent
                queue.append(i)
                visited[i] = True
    return answer[1:]


input = sys.stdin.readline

n = int(input())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    x, y = list(map(int, input().split()))
    tree[x].append(y)
    tree[y].append(x)

answer = BFS()
for i in answer:
    print(i)