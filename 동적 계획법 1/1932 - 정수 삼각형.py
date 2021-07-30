n = int(input())

triangle = []
for i in range(n):
    numbers = list(map(int, input().split()))
    triangle.append(numbers)

idx = 2
for i in range(1, n):
    for j in range(idx):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif i == j:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    idx += 1

print(max(triangle[-1]))