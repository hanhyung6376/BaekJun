import math

def isPrime(num):
    if(num==1):
        return False
    for j in range(2, int(math.sqrt(num))+1):
        if (num%j == 0):
            return False
    return True

prime = [0]* 10001


for i in range(1, 10001):
    if isPrime(i):
        prime[i] +=1

TC = int(input())


for i in range(TC):
    p = int(input())

    for j in range(0,p):
        if(prime[int(p/2)-j]==1 and prime[int(p/2)+j]==1):
            if(2*int(p/2)==p):
                print(int(p/2)-j, int(p/2)+j)
                break
