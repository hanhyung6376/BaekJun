num = int(input())


for i in range(num):
    avg = 0
    cnt = 0
    array = list(map(int, input().split()))
    for j in range(1 , len(array)):
        avg += array[j]
    avg /= array[0]
    for j in range(1, len(array)):
        if(array[j]> avg):
            cnt+=1
    print('%0.3f' %round(((cnt/array[0])*100),3)+"%")
