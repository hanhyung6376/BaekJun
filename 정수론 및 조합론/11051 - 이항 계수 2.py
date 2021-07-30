import sys

factorial = [0] * 1002
factorial[0:2] = 1, 1, 2


for i in range(3,len(factorial)):
    factorial[i] = factorial[i-1] * i

N, K = map(int, sys.stdin.readline().split())

result = factorial[N] // (factorial[K] * factorial[N-K])
print(result % 10007)
