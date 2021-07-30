import sys
while 1:
    tc1, tc2 = map(int, sys.stdin.readline().split())

    if tc1 == 0 and tc2 == 0:
        break

    if tc2 % tc1 == 0:
        print('factor')
    elif tc1 % tc2 == 0:
        print('multiple')
    else:
        print('neither')