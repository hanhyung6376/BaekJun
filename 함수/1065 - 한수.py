def hansu(a):
    array = list(str(a))
    if(a<=99):
        return 1
    elif(int(int(array[0]) - int(array[1])) == int(int(array[1]) - int(array[2]))):
        return 1
    else:
        return 0
cnt = 0
user = int(input())
for i in range (1, user+1):
    if(hansu(i)==1):
        cnt += 1
print(cnt)