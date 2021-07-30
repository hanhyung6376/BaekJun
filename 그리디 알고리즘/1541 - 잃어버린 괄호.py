numerical = input().split('-')

num = []
for i in numerical:
    n = i.split('+')
    result = 0
    for j in n:
        result += int(j)
    num.append(result)
result = num[0]

for i in range(1, len(num)):
    result -= num[i]
print(result)