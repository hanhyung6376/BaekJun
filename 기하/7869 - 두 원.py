import sys
import math
input = sys.stdin.readline
x1, y1, r1, x2, y2, r2 = map(float, input().split())

d= math.sqrt((x1- x2)**2 + (y1 - y2)**2)

# 두 원의 반지름의 합 보다 거리가 먼 경우
if d >= r1+ r2:
    answer = 0

# 원 속에 원이 있는 경우
elif d <= abs(r1 - r2):
    answer = math.pi * (min(r1, r2) ** 2)

else:
    x = (r1**2 - r2**2 + d**2) / (2*d)
    y = math.sqrt(r1**2 - x**2)
    theta1 = math.atan2(y, x) / math.pi * 180
    theta2 = math.atan2(y, d-x) / math.pi * 180
    answer = ((math.pi * (r1 ** 2) * theta1) / 180) + ((math.pi * (r2**2) * theta2) / 180) - (d*y)

print("%.3f" % answer)
