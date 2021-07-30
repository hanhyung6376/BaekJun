import sys

def mergesplit(num_list):
    if len(num_list) <= 1:
        return num_list

    mid = len(num_list) // 2
    left = mergesplit(num_list[:mid])
    right = mergesplit(num_list[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while len(left) > left_index and len(right) > right_index:
        if left[left_index] > right[right_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1
    while len(left) > left_index:
        result.append(left[left_index])
        left_index += 1
    while len(right) > right_index:
        result.append(right[right_index])
        right_index += 1
    return result


num = int(sys.stdin.readline())
number = []
for i in range(0, num):
    number.append(int(sys.stdin.readline()))

for i in mergesplit(number):
    print(i)