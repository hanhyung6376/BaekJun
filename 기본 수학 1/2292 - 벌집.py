num = int(input())
sum=0; i=0

while(1):
    if ((1 + (6 * i) + sum) >= num):
        break
    sum += (6 * i)
    i +=1

print(i+1)