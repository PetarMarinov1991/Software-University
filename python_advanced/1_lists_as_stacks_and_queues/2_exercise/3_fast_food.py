from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while food_quantity >= orders[0]:
    food_quantity -= orders.popleft()
    if not orders:
        print('Orders complete')
        exit(0)

print(f'Orders left: {" ".join([str(x) for x in orders])}')
