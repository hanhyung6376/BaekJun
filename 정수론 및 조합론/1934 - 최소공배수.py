import sys

def multiple(n, m):
    a = max(n, m)
    b = min(n, m)
    ab = a * b
    c = 1
    while 1:
        c = a % b
        if c == 0:
            result = b
            break
        a = b
        b = c

    return int(ab / result)

tc = int(sys.stdin.readline())
for i in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    sys.stdout.write("%s\n" % multiple(n, m))