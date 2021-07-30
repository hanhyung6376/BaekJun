import sys

tc = int(sys.stdin.readline())

for i in range(tc):
    N, M = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))
    seq = [i for i in range(N)]
    queue = []
    result = []
    idx = 0
    while 1:
        if priority[0] == max(priority):
            idx += 1
            if seq[0] == M:
                print(idx)
                break
            priority.pop(0)
            seq.pop(0)
        else:
            priority.append(priority.pop(0))
            seq.append(seq.pop(0))