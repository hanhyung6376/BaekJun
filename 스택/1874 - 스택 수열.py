import sys

def stack_check(numbers, num):
    stack_str = []
    stack1 = []
    stack2 = []
    for i in range(1, num+2):
        if len(stack1) >= 1 and numbers[0] == stack1[-1]:
            stack_str.append('-')
            stack1.pop()
            stack2.append(numbers.pop(0))
            while 1:
                if len(stack1) >= 1 and numbers[0] == stack1[-1]:
                    stack_str.append('-')
                    stack1.pop()
                    stack2.append(numbers.pop(0))
                else:
                    break
            if i <= num:
                stack1.append(i)
                stack_str.append('+')
        else:
            stack1.append(i)
            stack_str.append('+')
    if len(stack1) == 0:
        print("\n".join(stack_str))
    else:
        print('NO')

num = int(input())
numbers = []
for i in range(num):
    numbers.append(int(sys.stdin.readline()))

stack_check(numbers, num)