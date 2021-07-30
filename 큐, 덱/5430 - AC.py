import sys

def check(com, queue, n):
    com.replace('RR', '')
    right = 0
    left = 0
    lr = True
    for c in com:
        if c == 'R':
            lr = not lr
        elif c == 'D':
            if lr:
                left += 1
            else:
                right += 1


    if left + right <= n:
        queue = queue[left:n - right]
        if lr == False:
            queue.reverse()
        print(str(queue).replace(' ', ''))
    else:
        print('error')
        return


tc = int(sys.stdin.readline())

for i in range(tc):
    com = sys.stdin.readline()
    n = int(sys.stdin.readline())
    queue = eval(sys.stdin.readline())
    check(com, queue, n)