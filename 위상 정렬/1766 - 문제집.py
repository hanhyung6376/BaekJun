import heapq
import sys

def topology():
    heap = []
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        score = heapq.heappop(heap)
        result.append(score)
        for y in arr[score]:
            indegree[y] -= 1
            if indegree[y] == 0:
                heapq.heappush(heap, y)
    return result


input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for i in range(n+1)]
indegree = [0] * (n+1)


for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    indegree[y] += 1

print(*topology())
