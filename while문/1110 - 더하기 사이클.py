num = int(input())
i=0
if num<10:
    num*10
result = num

while(1):
    num = ((num%10)*10)+((int(num/10) + (num%10))%10)
    i+=1
    if(num==result):
        break;

print(i)