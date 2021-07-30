import sys

# 에라토스 테네스의 체
def prime_number(n):
    numbers = [True for i in range(n)]
    m = int(n ** 0.5)
    for i in range(2, m+1):
         if numbers[i]:
             for j in range(i+i, n, i):
                 numbers[j] = False
    return [i for i in range(2, n) if numbers[i] == True]

input = sys.stdin.readline
n  = int(input())
prime= prime_number(n+1)
start, end , result = 0, 1, 0

while end <= len(prime):
    temp = sum(prime[start:end])

    if temp == n:
        result += 1
        end +=1
    if temp < n:
        end += 1
    else:
        start += 1
print(result)