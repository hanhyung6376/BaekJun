import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

start, end = 0, n-1
result = [start, end]
x = abs(numbers[start] + numbers[end])
while start < end:
    temp = numbers[start] + numbers[end]

    if abs(temp) < x:
        result = [start, end]
        x = abs(temp)

    if temp == 0:
        result = [start, end]
        break
    elif temp <= 0:
        start += 1
    else:
        end -= 1

answer = [numbers[result[0]], numbers[result[1]]]
answer.sort()
print(answer[0], answer[1])