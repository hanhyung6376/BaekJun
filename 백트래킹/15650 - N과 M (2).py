def DFS(cnt):
    if cnt == M:
        print(*arr)
        return
    for i in range(0, N):
        if check[i]:
            continue
        len(arr)
        if len(arr) >= 1:
            if arr[-1] < num_list[i]:
                check[i] = True
                arr.append(num_list[i])
                DFS(cnt + 1)
                arr.pop()
                check[i] = False
        else:
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