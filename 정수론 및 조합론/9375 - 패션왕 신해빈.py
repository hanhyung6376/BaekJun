import sys

tc = int(sys.stdin.readline())

for i in range(tc):
    n = int(sys.stdin.readline())
    dict = {}
    for j in range(n):
        c1, c2 = sys.stdin.readline().split()
        if c2 not in dict:
            dict[c2] = 1
        elif c2 in dict:
            dict[c2] += 1
    result = 1
    for d in dict.values():
        result *= d+1
    print(result-1)