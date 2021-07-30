import sys

def scale(weight, n, now, left, right):
    new = abs(left - right)
    if new not in possible:
        possible.append(new)
    if now == n:
        return
    if dp[now][new] == 0:
        scale(weight, n, now + 1, left + weight[now], right)
        scale(weight, n, now + 1, left, right + weight[now])
        scale(weight, n, now + 1, left, right)
        dp[now][new] = 1

input = sys.stdin.readline
n = int(input())
weights = list(map(int, input().split()))
m = int(input())
check_weights = list(map(int, input().split()))

possible = []
dp = [[0 for i in range(15001)] for j in range(n+1)]

scale(weights, n, 0, 0, 0)
for i in check_weights:
    if i in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')
