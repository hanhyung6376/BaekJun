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
    if ccw1*ccw2 ==0 and ccw3*ccw4 == 0:
        if min(p1[0], p2[0]) <= max(p3[0], p4[0]) and min(p3[0], p4[0]) <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= max(p3[1], p4[1]) and min(p3[1], p4[1]) <= max(p1[1], p2[1]):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)