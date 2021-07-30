import sys

N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

result = 0
check = 0 #
for i in range(1, len(price)):

    if price[check] < price[i]:
        result += distance[i-1] * price[check]
    elif price[check] >= price[i]:
        result += distance[i-1] * price[check]
        check = i
print(result)