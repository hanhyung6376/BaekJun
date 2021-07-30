import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
card_number = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
find_number = list(map(int, sys.stdin.readline().split()))
cnt = [0] * M
card_number.sort()
for i in range(len(find_number)):
    l = bisect_left(card_number, find_number[i])
    r = bisect_right(card_number, find_number[i])
    cnt[i] = r-l

for i in cnt:
    print(i, end=" ")