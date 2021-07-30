TC = int(input())
for i in range(TC):
    H, W, num = map(int, input().split())
    if(num%H == 0):
        print(H*100+int(num/H))
    else:
        print(((num%H)*100)+ int(num/H)+1)
