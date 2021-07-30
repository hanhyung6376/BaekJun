import sys
#퀵 정렬
def quick(xy):
    if len(xy) <= 1:
        return xy
    pivot = len(xy) // 2
    less, more, equal = [], [], []
    for each in xy:
        if each[1] < xy[pivot][1]:
            less.append(each)
        elif each[1] > xy[pivot][1]:
            more.append(each)
        else:
            if each[0] < xy[pivot][0]:
                less.append(each)
            elif each[0] > xy[pivot][0]:
                more.append(each)
            else:
                equal.append(each)
    return quick(less) + equal + quick(more)


cnt = int(sys.stdin.readline())
new_list = []
for i in range(0, cnt):
    new_list.append(sys.stdin.readline())

point = []
for i in new_list:
    temp = i.split()
    temp = list(map(int, temp))
    point.append(temp)

quick_list = quick(point)

for i in quick_list:
    sys.stdout.write('%s ' % i[0]  + '%s\n' %i[1])