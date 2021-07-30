sugar = int(input())
min=sugar

for i in range(0, int(sugar/5)+1):
    for j in range(0, int(sugar/3)+1):
        if (sugar == 5*i + 3*j):
            if (min> i+j):
                min = i+j

if (min == sugar):
    print(-1)
else:
    print(min)