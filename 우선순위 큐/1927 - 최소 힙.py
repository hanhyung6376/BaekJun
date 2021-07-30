import sys
import heapq

N = int(sys.stdin.readline())

queue = []
for i in range(N):
    n = int(sys.stdin.readline())
    if n >= 1:
        heapq.heappush(queue, n)
    elif n == 0:
        try:
            print(heapq.heappop(queue))
        except:
            print(0)