import sys

def Make(p, table):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j

def KMP(t, p, table):
    Make(p, table)
    j, count, size = 0, 0, len(p)
    result = []

    for i in range(len(t)):
        while j > 0 and t[i] != p[j]:
            j = table[j-1]
        if t[i] == p[j]:
            if j == size-1:
                count += 1
                result.append(i-size+2)
                j = table[j]
            else:
                j += 1
    return [count, result]

input = sys.stdin.readline

t = input().replace("\n", "")
p = input().replace("\n", "")
table = [0 for i in range(len(p))]
result = KMP(t, p, table)

print(result[0])
print(*result[1])