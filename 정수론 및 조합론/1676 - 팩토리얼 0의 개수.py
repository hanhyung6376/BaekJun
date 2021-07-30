import sys
from math import factorial

n = int(sys.stdin.readline())

fac = factorial(n)
fac = list(map(int, str(fac)))
result = 0
for i in range(len(fac)-1, 0, -1):
    if fac[i]==0:
        result +=1
    else:
        break
print(result)