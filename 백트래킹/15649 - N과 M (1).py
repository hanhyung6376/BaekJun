def DFS(cnt):
    if cnt == M:
        print(*arr)
        return
    for i in range(0, N):
        if check[i]:
            continue

        check[i] = True
        arr.append(num_list[i])
        DFS(cnt + 1)
        arr.pop()
        check[i] = False


N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]
check = [False] * N

arr = []

DFS(0)