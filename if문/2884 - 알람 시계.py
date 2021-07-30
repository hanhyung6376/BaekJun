a, b = map(int, input().split())

if b<45:
    a -= 1
    b = 60-(45-b)
else:
    b = b-45

if a==-1:
    a=23

print(a, b)
