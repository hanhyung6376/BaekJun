n = [0] * 101
n[0:5] = [1, 1, 1, 2, 2]


for i in range(5, len(n)):
    n[i] = n[i-1] + n[i-5]
tc = int(input())
for i in range(tc):
    number = int(input())
    print(n[number-1])