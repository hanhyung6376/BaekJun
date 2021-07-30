import collections
import sys

N, M = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
deq = collections.deque([i for i in range(1, N+1)])

result = 0
for i in range(0, M):
    if deq[0] == number[i]:
        deq.popleft()
    elif deq.index(number[i]) <= len(deq) - deq.index(number[i]):
        result += deq.index(number[i])
        deq.rotate(-deq.index(number[i]))
        deq.popleft()
    else:
        result += len(deq) - deq.index(number[i])
        deq.rotate((len(deq) - deq.index(number[i])))
        deq.popleft()

print(result)