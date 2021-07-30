num = int(input())
i=0; sum=0

for i in range(0, num+1):
    if(sum+i>=num):
        break
    sum += i

if(i%2!=0):
    str = str(((sum + i + 1) - num)) + '/' + str((num - sum))
    print(str)
else:
    str = str((num-sum))+'/'+str(((sum+i+1)-num))
    print(str)