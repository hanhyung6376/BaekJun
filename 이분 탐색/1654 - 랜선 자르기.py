import sys

N, K = list(map(int, sys.stdin.readline().split()))
length = []
for i in range(N):
    length.append(int(sys.stdin.readline()))
start ,end = 1, max(length)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in length:
        result += i // mid

    if result >= K:
        start = mid +1
    else:
        end = mid - 1

print(end)