import collections
import sys

N = int(sys.stdin.readline())

def is_empty(deq):
    if len(deq) == 0:
        return 1
    else:
        return 0

deq = collections.deque()
for i in range(N):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        command[1] = int(command[1])
    if command[0] == 'push_front':
        deq.appendleft(command[1])
    elif command[0] == 'push_back':
        deq.append(command[1])
    elif command[0] == 'pop_front':
        if is_empty(deq) == 1:
            print('-1')
        else:
            print(deq.popleft())
    elif command[0] == 'pop_back':
        if is_empty(deq) == 1:
            print('-1')
        else:
            print(deq.pop())
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        print(is_empty(deq))
    elif command[0] == 'front':
        if is_empty(deq) == 1:
            print('-1')
        else:
            print(deq[0])
    elif command[0] == 'back':
        if is_empty(deq) == 1:
            print('-1')
        else:
            print(deq[-1])
