num = list(map(int, input().split()))
A = str(num[0]); B = str(num[1])
a = A[::-1]; b = B[::-1]
if (a> b):
    print(a)
else:
    print(b)
