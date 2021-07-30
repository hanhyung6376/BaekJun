import collections
import sys

num, cnt= map(int, sys.stdin.readline().split())
queue = collections.deque([i+1 for i in range(0, num)])
yosepuse = []

while 1:
    if len(queue) == 0:
        break
    queue.rotate(-(cnt-1))
    yosepuse.append(queue.popleft())



print('<', end='')
print(*yosepuse, sep=', ', end = '')
print('>')
