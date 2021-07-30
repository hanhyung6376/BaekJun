import sys

tc = int(sys.stdin.readline())
num = []
fibo = [[0 for i in range(2)] for j in range(41)]
fibo[0] = [1, 0]
fibo[1] = [0, 1]
for i in range(2, 41):
    fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
    fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]

for i in range(tc):
    num.append(int(sys.stdin.readline()))

for i in num:
    print(fibo[i][0], fibo[i][1])