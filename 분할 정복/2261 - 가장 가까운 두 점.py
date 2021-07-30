import sys

def div_conn(start, end):
    if start == end:
        return float('inf')

    if end - start == 1:
        return calc_dist(point[0], point[1])
    mid = (start + end) // 2

    # 분할정복으로 양쪽 구역에서 구해지는 거리 최솟값을 저장
    min_dist = min(div_conn(start, mid), div_conn(mid, end))


    temp = []
    # x축 기준 후보 점들 찾기
    for i in range(start, end+1):
        # 경계선을 기준으로 x 좌표가 최소거리보다 작은 점들만 포함
        if (point[mid][0] - point[i][0]) ** 2 < min_dist:
            temp.append(point[i])
    temp.sort(key = lambda x: x[1])
    # y축 기준 후보 점들 찾기
    for i in range(len(temp) - 1):
        for j in range(i+1, len(temp)):
            if (temp[i][1] - temp[j][1]) ** 2 < min_dist:
                min_dist = min(min_dist, calc_dist(temp[i], temp[j]))
            else:
                # 현재 후보 점이 다음 점과 최소 거리보다 멀다면 break
                break
    return min_dist


def calc_dist(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

input = sys.stdin.readline

n = int(input())
point = []
for i in range(n):
    point.append(list(map(int, input().split())))

point.sort(key = lambda x:x[0])

print(div_conn(0, n-1))