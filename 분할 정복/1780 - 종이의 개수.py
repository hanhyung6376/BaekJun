import sys

def div_con(x, y, n):
    global count, paper
    num = paper[x][y]
    check = 0
    for i in range(x, x+n):
        if check != 0:
            break
        for j in range(y, y+n):
            if num != paper[i][j]:
                div_con(x, y, n//3)
                div_con(x, y+(n//3), n//3)
                div_con(x, y+(2*(n//3)), n//3)

                div_con(x+(n//3), y, n//3)
                div_con(x+(n//3), y + (n // 3), n // 3)
                div_con(x+(n//3), y + (2 * (n // 3)), n // 3)

                div_con(x + (2 *(n // 3)), y, n // 3)
                div_con(x + (2 *(n // 3)), y + (n // 3), n // 3)
                div_con(x + (2* (n // 3)), y + (2 * (n // 3)), n // 3)

                check = 1
                break

    if check == 0 and num == -1:
        count[0] += 1
    elif check == 0 and num == 0:
        count[1] += 1
    elif check == 0 and num == 1:
        count[2] += 1

N = int(sys.stdin.readline())
count = [0] * 3
paper = []
for i in range(N):
    p = list(map(int, sys.stdin.readline().split()))
    paper.append(p)


div_con(0, 0, N)
for i in count:
    print(i)