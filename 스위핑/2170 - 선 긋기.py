import sys

input = sys.stdin.readline

n = int(input())

point = []
for i in range(n):
    x, y = map(int, input().split())
    point.append([x, y])

point.sort()
now = -float('inf')

result = 0

for i in range(n):
    start, end = point[i]
    if now < start:
        now = start
    if now < end:
        result += end - now
        now = end
print(result)