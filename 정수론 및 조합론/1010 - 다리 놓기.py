import sys
from math import factorial

tc = int(sys.stdin.readline())

for i in range(tc):
    N, M = map(int, sys.stdin.readline().split())
    result = 1
    result = factorial(M) // (factorial(N) * factorial(M-N))
    print(result)