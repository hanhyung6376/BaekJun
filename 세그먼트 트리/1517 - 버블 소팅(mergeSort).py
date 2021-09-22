# 병합 정렬 풀이
import sys

def mergeSort(start, end):
    global count
    if start < end:
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid+1, end)

        left = start
        right = mid + 1
        tmp = []
        while left <= mid and right <= end:
            if arr[left] <= arr[right]:
                tmp.append(arr[left])
                left += 1
            else:
                tmp.append(arr[right])
                right += 1
                count += (mid - left + 1)
        if left <= mid:
            tmp += arr[left:mid+1]
        if right <= end:
            tmp += arr[right:end+1]

        for i in range(len(tmp)):
            arr[start + i] = tmp[i]


input = sys.stdin.readline
count = 0
n = int(input())
arr = list(map(int, input().split()))
mergeSort(0, n-1)
print(count)