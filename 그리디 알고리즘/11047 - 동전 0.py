N, K = map(int, input().split())

price = []
for i in range(N):
    p = int(input())
    if p > K:
        continue
    else:
        price.append(p)

cnt = 0
while 1:
    cnt += K//price[-1]
    K -= (K//price[-1]) * price[-1]
    if K == 0:
        print(cnt)
        break
    else:
        price.pop()