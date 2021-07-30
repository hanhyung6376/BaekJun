import sys
from collections import Counter
def quick(num):
    if len(num) < 1:
        return num
    pivot = num[len(num) // 2]
    less, equal, more = [], [], []

    for each in num:
        if each < pivot:
            less.append(each)
        elif each > pivot:
            more.append(each)
        else:
            equal.append(each)
    return quick(less) + equal + quick(more)

def many_value(v):
    if cnt == 1: return v[0]
    c = Counter(v).most_common(2)
    return (c[1][0] if c[0][1] == c[1][1] else c[0][0])

cnt = int(sys.stdin.readline())
num = []
sum = 0
for i in range (0,cnt):
    num.append(int(sys.stdin.readline()))
    sum += num[-1]

sort_list = quick(num)



sys.stdout.write('%s\n' % round(sum/cnt))
sys.stdout.write('%s\n' % sort_list[len(sort_list) // 2])
sys.stdout.write('%s\n' % many_value(sort_list))
sys.stdout.write('%s\n' % (sort_list[-1]-sort_list[0]))