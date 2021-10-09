import sys

input = sys.stdin.readline

m = int(input())
f = [0] + list(map(int, input().split()))
q = int(input())
dp = [[f[i]] for i in range(m + 1)]

# sparse table
for i in range(1, 19):
     for j in range(1, m+1):
          dp[j].append(dp[dp[j][i-1]][i-1])

for i in range(q):
     n, x = map(int, input().split())
     for j in range(18, -1, -1):
          if n>= 1 << j:
               n -= 1 << j
               x = dp[x][j]
     print(x)
