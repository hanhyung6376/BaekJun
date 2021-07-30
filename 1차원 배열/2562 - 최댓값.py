array = []
num = 0
while (1):
    for i in range(9):
        array.append(int(input()))
    if (max(array) < 100):
        break

print(max(array))
print(array.index(max(array)) + 1)