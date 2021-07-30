TC1 = int(input())
TC2 = int(input())
sum = 0
min = TC2

for i in range(TC1,TC2+1):
    div = 0
    for j in range(1, i):

        if(i%j==0):
            div+=1
    if(div ==1):
        sum += i
        if(min > i):
            min = i

if(sum != 0):
    print(sum)
    print(min)
else:
    print(-1)