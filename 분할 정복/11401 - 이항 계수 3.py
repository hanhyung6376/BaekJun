import sys

def div_con(n, p):
    prime = 1000000007
    if p == 0:
        return 1
    temp = div_con(n, p//2)
    if p % 2 == 0:
        return (temp * temp) % prime
    elif p % 2 == 1:
        return (temp * temp * n) % prime

p = 1000000007
N, K = map(int, sys.stdin.readline().split())
factorial = [0] * (N+1)
factorial[0:1] = 1, 1
for i in range(2,N+1):
    factorial[i]  = factorial[i-1] * i % p
a = factorial[N]
b = factorial[K] * factorial[N-K]
result = ((a % p) * div_con(b % p, p-2)) % p
print(result)