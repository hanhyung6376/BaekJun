import sys

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
    return quick(more) + equal + quick(less)

num = sys.stdin.readline().strip()
num = list(num)
num = list(map(int, num))
q = quick(num)
q = ''.join(map(str, q))
sys.stdout.write('%s\n' % q)
