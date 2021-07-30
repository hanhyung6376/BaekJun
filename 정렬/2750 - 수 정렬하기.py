num = int(input()); array = []

for i in range(num):
    array.append(int(input()))
array.sort()

for i in range (0, num):
    print(array[i])
