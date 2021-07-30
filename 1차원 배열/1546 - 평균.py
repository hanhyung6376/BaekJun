num = int(input())
array = list(map(int, input().split()))
avg = 0

for i in range(0, num):
    avg += (array[i]/max(array))*100

print(avg/num)