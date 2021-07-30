array = []
res = 1;

while (1):
    a = int(input())
    b = int(input())
    c = int(input())
    if ((a >= 100 and a < 1000) and (b >= 100 and b < 1000) and (a >= 100 and a < 1000)):
        break;
a *= b * c
while (1):
    if (res > a):
        res /= 10
        break;
    else:
        res *= 10

for i in range(10):
    array.append(0)

while (1):
    if (res < 1):
        break;
    array[int(a / res)] += 1
    a -= int(a / res) * res
    res /= 10

for i in range(0, 10):
    print(array[i])