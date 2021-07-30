import sys


def empty():
    if len(queue) <= cnt:
        return 1
    else:
        return 0

def front():
    if empty() == 1:
        sys.stdout.write('%s\n' % -1)
    else:
        sys.stdout.write('%s\n' % queue[cnt])


def back():
    if empty() == 1:
        sys.stdout.write('%s\n' % -1)
    else:
        sys.stdout.write('%s\n' % queue[-1])

queue = []
rep = int(sys.stdin.readline())
cnt = 0
for i in range(rep):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        queue.append(a[1])
    elif a[0] == 'pop':
        if cnt < len(queue):
            print(queue[cnt])
            cnt += 1
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(queue) - cnt )
    elif a[0] == 'empty':
        sys.stdout.write('%s\n' % empty())
    elif a[0] == 'front':
        front()
    elif a[0] == 'back':
        back()
    del a
