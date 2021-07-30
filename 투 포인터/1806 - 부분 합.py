import sys

input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
start, end = 0, 0
length = n+1
num = 0
while 1:
    if num >= s:
        length = min(length, end - start)
        num -= numbers[start]
        start += 1
    elif end == n:
        break;
    else:
        num += numbers[end]
        end +=1

print(length if length != n+1 else 0)