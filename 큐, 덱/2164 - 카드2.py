import collections
import sys

num = int(sys.stdin.readline())
queue = collections.deque([i+1 for i in range(0, num)])
cnt = 1
while 1:
    if len(queue) == 1:
        break

    if cnt % 2 == 1:
        queue.popleft()
    else:
        queue.rotate(-1)
    cnt += 1