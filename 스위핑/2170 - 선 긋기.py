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
    s, e = point[i]
    if now < s:
        now = s
    if now < e:
        result += e - now
        now = e
print(result)