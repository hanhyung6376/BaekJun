import sys

N = int(sys.stdin.readline())
person = list(map(int, sys.stdin.readline().split()))

person.sort()

cnt = 0
result = 0
for i in person:
    cnt += i
    result += cnt
print(result)