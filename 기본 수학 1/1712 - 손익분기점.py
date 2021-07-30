salary, cost, price = map(int, input().split())

if(cost < price):
    print(int(salary/(price-cost) + 1))
else:
    print(-1)