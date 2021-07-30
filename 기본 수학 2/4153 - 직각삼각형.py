def triangle(a, b, c):
    if(a*a == b*b + c*c or b*b== a*a + c*c or c*c == a*a + b*b):
        print("right")
    else:
        print("wrong")

while(1):
    a, b, c = map(int, input().split())
    if(a==0 and b==0 and c==0):
        break
    else:
        triangle(a, b, c)
