def time(a):
    sec =0
    b = ord(a)
    if(b>=65 and b<=67):
       return 3
    elif(b>=68 and b<=70):
        return 4
    elif(b>=71 and b<=73):
        return 5
    elif(b>=74 and b<=76):
        return 6
    elif (b >= 77 and b <= 79):
        return 7
    elif (b >= 80 and b <= 83):
        return 8
    elif (b >= 84 and b <= 86):
        return 9
    elif (b >= 87 and b <= 90):
        return 10


dial = list(input())
sum = 0
for i in range(0,len(dial)):
    sum += time(dial[i])
print(sum)