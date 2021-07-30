n = int(input())

cost = [[0 for i in range(3)] for j in range(n)]
color_cost = []
for i in range(n):
    color = list(map(int, input().split()))
    color_cost.append(color)

cost[0] = color_cost[0]

for i in range(1, n):
    cost[i][0] = min(cost[i-1][1] + color_cost[i][0], cost[i-1][2] + color_cost[i][0])
    cost[i][1] = min(cost[i-1][0] + color_cost[i][1], cost[i-1][2] + color_cost[i][1])
    cost[i][2] = min(cost[i-1][0] + color_cost[i][2], cost[i-1][1] + color_cost[i][2])

print(min(cost[-1]))