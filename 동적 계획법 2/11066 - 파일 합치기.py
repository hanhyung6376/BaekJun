import sys

def knuth_optimizer():
    dp = [[0 for col in range(file_count+1)] for row in range(file_count+1)]
    file_sum = [0] * (file_count+1)

    for i in range(1, file_count+1):
        file_sum[i] = file_sum[i-1] + file_list[i]

    # 파일의 길이가 1일 경우에는 비용이 들지 않으므로 2부터 시작
    for i in range(2, file_count+1):
        for j in range(1, file_count+2-i):
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (file_sum[j+i-1] - file_sum[j-1])

    return dp[1][file_count]

input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    file_count = int(input())
    file_list = [0] + list(map(int, input().split()))
    print(knuth_optimizer())
