word = list(input())
alpha = []

for i in range (97, 123):
    alpha.append(chr(i))

alpha2 = [-1] * 26

for i in range(0, len(word)):
    for j in range(0, 26):
        if(alpha[j] == word[i]):
            if(alpha2[j] == -1):
                alpha2[j] += i+1
for i in range(0, 26):
    print(alpha2[i], end=" ")