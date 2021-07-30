cnt=0; array = []

for i in range(42):
    array.append(0)

for i in range(10):
    a = int(input())
    array[a%42] += 1

for i in range(42):
    if(array[i]>0):
        cnt +=1
print(cnt)
