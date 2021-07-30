import sys
import itertools

def calc(comb, stats):
    start = comb[0:len(comb)//2]
    link = comb[len(comb)//2:]
    link.reverse()
    result = 100
    for s, l in zip(start, link):
        sc = itertools.combinations(s, 2)
        lc = itertools.combinations(l, 2)
        s_score = 0
        l_score = 0
        for i, j in zip(sc, lc):
            s_score += stats[i[0]][i[1]] + stats[i[1]][i[0]]
            l_score += stats[j[0]][j[1]] + stats[j[1]][j[0]]
        score = abs(s_score - l_score)
        if score == 0:
            return 0
        elif score < result:
            result = score
    return result


N = int(sys.stdin.readline())
com = [i for i in range(N)]

stats = []
for i in range(N):
    s = list(map(int, sys.stdin.readline().split()))
    stats.append(s)

comb = itertools.combinations(com, N//2)
print(calc(list(comb), stats))
