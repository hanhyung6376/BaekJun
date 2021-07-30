import math
def fly(year):
    min = int(math.sqrt(year))
    if(year==min*min):
        min = 2*min-1
    elif(year<=min*min+min):
        min = 2*min
    else:
        min=2*min+1
    return min

TC= int(input())

for i in range(TC):
    x, y = map(int, input().split())
    print(fly(y-x))