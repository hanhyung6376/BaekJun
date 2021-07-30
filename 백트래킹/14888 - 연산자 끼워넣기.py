import sys
import itertools

N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
op = ''
op += '+' * operator[0]
op += '-' * operator[1]
op += '*' * operator[2]
op += '/' * operator[3]

op = list(op)
op_combination = set(itertools.permutations(op, N-1))
idx = 0
max, min = -1000000000, 1000000000
for o in op_combination:
    idx = 0
    result = number[0]
    for n in range(1, len(number)):
        if o[idx] == '+':
            result += number[n]
        elif o[idx] == '-':
            result -= number[n]
        elif o[idx] == '*':
            result *= number[n]
        elif o[idx] == '/':
            if result < 0 and number[n] > 0:
                result = (abs(result) // number[n]) * -1
            else:
                result = result // number[n]

        idx += 1
    if result > max:
        max = result

    if result < min:
        min = result

print(int(max))
print(int(min))