import sys


def pop():
    if empty() == 1:
        print(-1)
    else:
        print(stack[-1])
        del stack[-1]

def size():
    print(len(stack))

def empty():
    if len(stack) <1:
        return 1
    else:
        return 0

def top():
    if empty() == 0:
        print(stack[-1])
    else:
        print(-1)

cnt = int(input())
stack = []
for i in range(cnt):
    a = sys.stdin.readline().split()
    if len(a) == 2:
        a[1] = int(a[1])
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'pop':
        pop()
    elif a[0] == 'top':
        top()
    elif a[0] == 'size':
        size()
    elif a[0] == 'empty':
        print(empty())
    elif a[0] == 'top':
        top()
