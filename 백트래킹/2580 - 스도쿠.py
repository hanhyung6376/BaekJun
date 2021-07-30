import sys

def DFS(x):
    global isTrue

    # 이미 답이 출력된 경우
    if isTrue:
        return
    if x == len(zero):
        for i in matrix:
            for j in i:
                print(j, end=' ')
            print()
        isTrue = True
        return
    else:
        (dx, dy) = zero[x]
        answers = check(dx, dy) # 정답 리스트

        for i in answers:
            matrix[dx][dy] = i # 정답 리스트 중 하나를 대입
            DFS(x+1) # 다음 0으로 넘어감
            matrix[dx][dy] = 0 # 정답이 아닐 경우 초기화
def check(x, y):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 가로 세로 검사
    for i in range(9):
        if matrix[x][i] in numbers:
            numbers.remove(matrix[x][i])
        if matrix[i][y] in numbers:
            numbers.remove(matrix[i][y])

    # 3*3 칸 검사
    x = x//3
    y = y//3

    for nx in range(x*3, (x+1)*3):
        for ny in range(y*3, (y+1)*3):
            if matrix[nx][ny] in numbers:
                numbers.remove(matrix[nx][ny])
    return numbers

input = sys.stdin.readline
matrix = [list(map(int, input().split())) for i in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if matrix[i][j] == 0] # 0의 위치
isTrue = False # 정답이 완성 되었는지 체크

DFS(0)
