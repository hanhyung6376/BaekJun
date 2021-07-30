import sys
import heapq

N = int(sys.stdin.readline())

queue = []
for i in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(queue, (abs(n), n))
    elif n == 0:
        try:
            print(heapq.heappop(queue)[1])
        except:
            print(0)