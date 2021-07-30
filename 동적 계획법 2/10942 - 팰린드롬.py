import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tc = int(input())
dp = [[0 if i != j else 1 for i in range(n)] for j in range(n)]

for i in range(n):
    for start in range(n):
        end = start + i
        if end >= n:
            break
        if dp[start][end] == 0:
            if start+1 == end:
                if arr[start] == arr[end]:
                    dp[start][end] = 1
                    continue
            if arr[start] == arr[end] and dp[start+1][end-1]:
                dp[start][end] = 1

for i in range(tc):
    x, y = map(int, input().split())
    print(dp[x-1][y-1])