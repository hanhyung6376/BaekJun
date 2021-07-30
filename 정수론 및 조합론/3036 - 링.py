import sys
import fractions

N = int(sys.stdin.readline())
ring = list(map(int, sys.stdin.readline().split()))

for i in range(1,len(ring)):
    a = fractions.Fraction(ring[0], ring[i])
    a = str(a)
    if '/' not in a:
        a += '/1'
    print(a)