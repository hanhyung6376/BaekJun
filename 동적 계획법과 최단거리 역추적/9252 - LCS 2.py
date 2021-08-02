import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()
dp = [[[0, []] for i in range(len(a) + 1)] for j in range(len(b) + 1 )]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[j+1][i+1][0] = dp[j][i][0] + 1
            dp[j+1][i+1][1] = dp[j][i][1] + [b[j]]
        else:
            dp[j+1][i+1][0] = max(dp[j][i+1][0], dp[j+1][i][0])
            if dp[j+1][i+1][0] == dp[j][i+1][0]:
                dp[j+1][i+1][1] = dp[j][i+1][1]
            elif dp[j+1][i+1][0] == dp[j+1][i][0]:
                dp[j + 1][i + 1][1] = dp[j+1][i][1]


print(dp[len(b)][len(a)][0])
for i in dp[len(b)][len(a)][1]:
    print(i, end='')