import math

def isPrime(num):
    if(num==1):
        return False
    for j in range(2, int(math.sqrt(num))+1):
        if (num%j == 0):
            return False
    return True


TC1 ,TC2 = map(int, input().split())
for i in range(TC1, TC2+1):
    if isPrime(i):
        print(i)