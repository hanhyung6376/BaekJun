import sys

def div_con(num, index):
    if index == 1:
        return num % C
    power = div_con(num, index//2)
    if index%2 == 0:
        return power * power % C
    elif index%2 == 1:
        return power * power * num % C


A, B, C = map(int, sys.stdin.readline().split())

print(int(div_con(A, B)))