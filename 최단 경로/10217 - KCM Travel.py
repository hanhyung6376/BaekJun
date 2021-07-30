import sys

def dijkstra(start):
    dp[start][0] = 0
    for cost in range(M+1):
        for edge in range(1, N+1):
            # 방문하는 dp가 inf 면 생략
            if dp[edge][cost] == inf:
                continue
            now_time = dp[edge][cost] # 현재 소요시간
            for next, next_cost, next_time in graph[edge]:
                # 현재까지의 코스트와 다음 방문에 소요되는 코스트가 총 코스트를 넘으면 생략
                if next_cost + cost > M:
                    continue
                # 방문할려는 위치 ,현재의 코스트 + 방문하기 위한 코스트 값 중 최솟값
                # 다음 방문할려는 곳이 한번도 방문을 안했다면 해당 값이 inf이므로 now_time + next_time으로 갱신됨
                # 그러나 한번 방문된 곳이라면 2가지의 경우의 수 중 최솟 값으로 갱신
                dp[next][next_cost + cost] = min(dp[next][next_cost + cost], now_time + next_time)


input = sys.stdin.readline
inf = float('inf')
tc = int(input())
for i in range(tc):
    N, M, K = map(int, input().split())
    dp = [[inf for r in range(M+1)] for c in range(N+1)]
    graph = [[] for i in range(N+1)]
    for j in range(K):
        # c = 비용, d = 소요시간
        u, v, c, d = map(int, input().split())
        graph[u].append([v, c, d])
    dijkstra(1)
    result = min(dp[N])

    print(result if result != inf else 'Poor KCM' )