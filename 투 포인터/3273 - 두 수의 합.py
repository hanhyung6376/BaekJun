import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

x = int(input())
sum = 0
result = 0
start = 0
end = n-1
while start < end:
    temp = numbers[start] + numbers[end]
    if temp == x:
        result += 1
        start +=1
    elif temp < x:
        start +=1
    else:
        end -= 1
print(result)