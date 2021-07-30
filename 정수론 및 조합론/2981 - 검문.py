import sys
from math import gcd

N = int(sys.stdin.readline())
number = []
for i in range(N):
    number.append(int(sys.stdin.readline()))
number = sorted(number)

result = number[1] - number[0]
for i in range(2, N):
    a = number[i] - number[i-1]
    result = gcd(result, a)

M = []
for i in range(2, int(result**(1/2)) + 1):
    if result % i == 0:
        M.append(i)
        M.append(result//i)
M.append(result)
M = list(set(M))
M.sort()
for i in M:
    print(i, end=' ')