import sys

def div_con(x, y, n):
    global compression, paper
    color = paper[x][y]
    check = 0
    for i in range(x, x+n):
        if check != 0:
            break
        for j in range(y, y+n):
            if color != paper[i][j]:
                compression += '('
                div_con(x, y, n//2)  # 2사분면
                div_con(x, y+(n//2), n//2) # 1사분면
                div_con(x+(n//2), y , n // 2 )  # 3사분면
                div_con(x+(n//2), y+(n//2), n//2)       # 4사분면
                check = 1
                compression += ')'
                break

    if check == 0 and color == '0':
        compression += '0'
    elif check == 0 and color == '1':
        compression += '1'

N = int(sys.stdin.readline())
compression = ''
paper = []
for i in range(N):
    p = sys.stdin.readline().strip()
    p = list(p)
    paper.append(p)


div_con(0, 0, N)
print(compression)