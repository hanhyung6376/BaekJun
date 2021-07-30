import math

TC = int(input())

for i in range(TC):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    if(x1==x2 and y1==y2):
        if(r1==r2):
            print(-1)
        else:
            print(0)
        continue

    if(distance==r1+r2 or r2 == r1+distance or r1 == distance+r2):
        print(1)
    elif(distance+r2<r1 or distance+r1<r2 or distance > r1 +r2):
        print(0)
    else:
        print(2)