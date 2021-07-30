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

# 행렬 곱
def matrix_multiple(temp1, temp2):
    result_matrix = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        for j in range(2):
            result_matrix[i][j] = multiple(i, j, temp1, temp2)
    return result_matrix

# 행렬 곱 연산
def multiple(x, y, temp1, temp2):
    result = 0
    mat2 = [mat[y] for mat in temp2]
    for i, j in zip(temp1[x], mat2):
        result += i * j
    return result % 1000000007

N= int(sys.stdin.readline())

matrix = [[1, 1], [1, 0]]

result = Square(N)
result = result[0][1]
print(result)