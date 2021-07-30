num = int(input())
x = 2
while(1):
    if(num == 1):
        break;
    elif(num%x >0):
        x += 1
    elif(num%x == 0):
        num /= x
        print(x)