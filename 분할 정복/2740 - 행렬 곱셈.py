import sys

def matrix_multiple(N, K):
    global matrix1, matrix2, result_matrix
    for i in range(N):
        for j in range(K):
            result_matrix[i][j] = multiple(i, j)

def multiple(x, y):
    result = 0
    mat2 = [mat[y] for mat in matrix2]
    for i, j in zip(matrix1[x], mat2):
        result += i*j
    return result
N, M = map(int, sys.stdin.readline().split())

matrix1 = []
matrix2 = []

for i in range(N):
    m = list(map(int, sys.stdin.readline().split()))
    matrix1.append(m)

M, K = map(int, sys.stdin.readline().split())
result_matrix = [[0 for i in range(K)] for j in range(N)]
for i in range(M):
    m = list(map(int, sys.stdin.readline().split()))
    matrix2.append(m)

matrix_multiple(N, K)
for i in result_matrix:
    for j in i:
        print(j, end=' ')
    print()