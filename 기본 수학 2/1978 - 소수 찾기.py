TC = int(input())
number = list(map(int, input().split()))
prime = 0

for i in range(0,TC):
    div = 0
    for j in range(1, number[i]):
        if(number[i]%j==0):
            div+=1
    if(div ==1):
        prime +=1

print(prime)