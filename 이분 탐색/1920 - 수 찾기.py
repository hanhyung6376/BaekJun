def binary_search(nums, n, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2

    if n == nums[mid]:
        return 1
    elif n < nums[mid]:
        return binary_search(nums, n, start, mid-1)
    else:
        return binary_search(nums, n, mid+1, end)


n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
f_n = int(input())
f_nums = list(map(int, input().split()))

for i in f_nums:
    start = 0
    end = len(nums) - 1
    print(binary_search(nums, i, start, end))