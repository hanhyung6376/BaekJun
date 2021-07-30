import sys
num = int(input())

for i in range(num):
    yn = 0
    str_list = []
    stack = []
    vps = sys.stdin.readline().rstrip()
    str_list = list(vps)
    for j in str_list:
        if j == '(':
            stack.append('(')
        else:
            if len(stack) >= 1 and stack.pop() == '(':
                pass
            else:
                yn = 1
                break
    if yn == 0 and len(stack) == 0:
        print('YES')
    else:
        print('NO')
    del str_list
    del stack