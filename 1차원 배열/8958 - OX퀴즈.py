num = int(input())

for i in range(0 ,num):
    array = input()
    ox = list(array)
    sum = 0
    cnt = 0
    for j in range(len(array)):
        if(ox[j] == 'O'):
            cnt +=1
            sum += cnt
        elif(ox[j]=='X'):
            cnt = 0
    print(sum)
