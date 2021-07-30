def hanoi(disk, start, end):
    if disk == 1:
        print(start, end)
        return

    hanoi(disk-1, start, 6-start-end)
    print(start, end)
    hanoi(disk-1, 6-start-end, end)


num = int(input())
print(2**num -1)
hanoi(num, 1, 3)