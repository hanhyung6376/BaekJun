import sys

setObj = set()
m = int(input())

for i in range(m):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'all':
        setObj = set([i for i in range(1, 21)])
        continue
    elif cmd[0] == 'empty':
        setObj = set()
        continue

    cmd, num = cmd[0], cmd[1]
    if cmd == 'add':
        setObj.add(int(num))
    elif cmd == 'remove':
        setObj.discard(int(num))
    elif cmd == 'check':
        if int(num) in setObj:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if int(num) in setObj:
            setObj.discard(int(num))
        else:
            setObj.add(int(num))
