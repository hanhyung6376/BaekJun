import sys

A = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
dp1 = [0] * A
dp2 = [0] * A
result = [0] * A
for i in range(A):
    for j in range(i):
        if seq[i] > seq[j] and dp1[i] < dp1[j]:
            dp1[i] = dp1[j]
    dp1[i] += 1
    result[i] += dp1[i]

for i in range(A-1, -1, -1):
    for j in range(A-1, i, -1):
        if seq[i] > seq[j] and dp2[i] < dp2[j]:
            dp2[i] = dp2[j]
    dp2[i] += 1
    result[i] += dp2[i]


print(max(result) - 1)