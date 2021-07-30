import sys

a, b, v = sys.stdin.readline().split()
a=int(a); b=int(b); v=int(v)
sum = (v - b) / (a - b)

if ((v - b) % (a - b) >= 1):
    sum+=1
print(int(sum))