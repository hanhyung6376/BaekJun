import sys

N, K = map(int, sys.stdin.readline().split())
house = []
for i in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()

start ,end = 1, max(house) - min(house)

while start <= end:
    mid = (start + end) // 2
    result = 1
    len = house[0]
    for i in house:
        if len + mid <= i:
            len = i
            result += 1
    if result >= K:
        start = mid +1
    else:
        end = mid - 1

print(end)