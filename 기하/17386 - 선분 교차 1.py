import sys

def ccw(a, b, c):
    result = ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0]-a[0]))
    return result



input = sys.stdin.readline

point = []
point.append(list(map(int, input().split())))
point.append(list(map(int, input().split())))
p1, p2, p3, p4 = point[0][0:2], point[0][2:4], point[1][0:2], point[1][2:4]
ccw1 = ccw(p1, p2, p3)
ccw2 = ccw(p1, p2, p4)
ccw3 = ccw(p3, p4, p1)
ccw4 = ccw(p3, p4, p2)

if ccw1*ccw2 <= 0 and ccw3*ccw4 <= 0:
    print(1)
else:
    print(0)