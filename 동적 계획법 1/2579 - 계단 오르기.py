import sys

n = int(sys.stdin.readline())
stair = [0]  * 301
dp = [0] * 301
for i in range(n):
    stair[i] = int(sys.stdin.readline())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[1] + stair[2], stair[0] + stair[2]) # 점프를 하고 그 다음 계단을 밟았을 경우, 첫 계단을 밟고 점프를 할 경우 중 최댓값
for i in range(3, n):
    dp[i] = max(dp[i-3] + stair[i - 1] + stair[i], dp[i-2] + stair[i]) # 마지막 계단 전 계단을 밟았을 경우, 마지막 계단 전 계단을 밟지 않았을 경우

print(dp[n-1])