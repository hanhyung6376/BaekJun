x,y,w,h = map(int, input().split())
point_1 = abs(w-x)
point_2 = abs(h-y)
print(min(point_1,point_2,x,y))
