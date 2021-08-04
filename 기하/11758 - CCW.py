import sys

input = sys.stdin.readline
x, y = [], []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

s = (x[1] - x[0])*(y[2] - y[0]) - (y[1] - y[0])*(x[2] - x[0])

if s == 0:
    print(0)
elif s < 0:
    print(-1)
else:
    print(1)
