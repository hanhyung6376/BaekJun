import sys

def Square(b):
    if b == 1:
        return matrix
    temp = Square(b // 2)
    if b % 2 == 0:
        result = matrix_multiple(temp,temp)
        return result
    elif b % 2 == 1:
        result = matrix_multiple(temp,temp)
        result = matrix_multiple(result, matrix)
        return result



def matrix_multiple(temp1, temp2):
    result_matrix = [[0 for i in range(N)] for j in range(N)]
    for i in range(len(temp1)):
        for j in range(len(temp1)):
            result_matrix[i][j] = multiple(i, j, temp1, temp2)
    return result_matrix

# 행렬 곱 연산
def multiple(x, y, temp1, temp2):
    result = 0
    mat2 = [mat[y] for mat in temp2]
    for i, j in zip(temp1[x], mat2):
        result += i * j
    return result % 1000

N, B = map(int, sys.stdin.readline().split())

matrix = []
for i in range(N):
    m = list(map(int, sys.stdin.readline().split()))
    matrix.append(m)

result = Square(B)
for i in result:
    for j in i:
        print(j % 1000, end= ' ')
    print()
