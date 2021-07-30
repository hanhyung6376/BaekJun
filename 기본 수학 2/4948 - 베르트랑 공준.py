import math

def isPrime(num):
    if(num==1):
        return False
    for j in range(2, int(math.sqrt(num))+1):
        if (num%j == 0):
            return False
    return True

prime = [0]* 246913
for i in range(1, 246913):
    if isPrime(i):
        prime[i] +=1


while(1):
    sum = 0
    TC = int(input())
    if(TC==0):
        break
    for i in range(TC+1, 2*TC+1):
        if(prime[i]==1):
            sum +=1

    print(sum)
