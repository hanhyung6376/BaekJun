import sys

def right_big_number(numbers, num):
    result = [-1] * num
    stack = []
    for i in range(num):
        try:
            while numbers[stack[-1]] < numbers[i]:
                result[stack.pop()] = numbers[i]
        except:
            pass
        stack.append(i)

    for i in result:
        print(i, end=' ')


num = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
right_big_number(numbers, num)