import sys
num = int(sys.stdin.readline())
n = [0] * 1000001
n[0] = 1
n[1] = 2

for i in range(2, num):
    n[i] = (n[i-1] + n[i-2])%15746
print(n[num-1])
