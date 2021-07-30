import sys

num = int(sys.stdin.readline())
num_list = list(map(int, input().split()))

sort_list = sorted(set(num_list))
dic = {sort_list[i] : i for i in range(len(sort_list))}

for i in num_list:
    print(dic[i], end=' ')