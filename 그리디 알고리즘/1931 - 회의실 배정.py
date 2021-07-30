import sys

N = int(sys.stdin.readline())

meeting = []
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    meeting.append([s, e])

meeting = sorted(meeting, key=lambda item: (item[1], item[0]))
cnt = 0
now = 0
for start, end in meeting:
    if start >= now:
        now = end
        cnt+= 1
print(cnt)