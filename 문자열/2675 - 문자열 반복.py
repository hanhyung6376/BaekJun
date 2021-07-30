T = int(input())

for i in range(T):
    R, S = input().split()
    array=str(S)
    for j in range (0, len(array)):
        print(array[j]*int(R), end="")
    print()
