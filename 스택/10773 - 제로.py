num = int(input())
num_list = []
result = 0
for i in range(num):
    n = int(input())
    if n == 0:
        result -= num_list[-1]
        del num_list[-1]
    else:
        result += n
        num_list.append(n)

print(result)