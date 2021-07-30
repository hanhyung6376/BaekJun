import sys

def div_con(x, y, n):
    global blue, white, paper
    color = paper[x][y]
    check = 0
    for i in range(x, x+n):
        if check != 0:
            break
        for j in range(y, y+n):
            if color != paper[i][j]:
                div_con(x, y, n//2)  # 2사분면
                div_con(x, y+(n//2), n//2) # 1사분면
                div_con(x+(n//2), y , n // 2 )  # 3사분면
                div_con(x+(n//2), y+(n//2), n//2)       # 4사분면
                check = 1
                break
    if check == 0 and color == 0:
        white += 1
    elif check == 0 and color == 1:
        blue += 1

N = int(sys.stdin.readline())
blue, white = 0, 0
paper = []
for i in range(N):
    p = list(map(int, sys.stdin.readline().split()))
    paper.append(p)

div_con(0, 0, N)
print(white)
print(blue)