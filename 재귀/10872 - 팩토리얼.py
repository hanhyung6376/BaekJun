def fact(n):
    if(n>=1):
        return n*fact(n-1)
    else:
        return 1

num = int(input())
print(fact(num))