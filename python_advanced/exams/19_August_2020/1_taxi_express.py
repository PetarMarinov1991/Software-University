from collections import deque

customers, taxis = [deque([int(x) for x in input().split(', ')]) for _ in range(2)]
total_time = 0

while customers:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()

    if current_customer <= current_taxi:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)

    if not taxis and customers:
        print(f'Not all customers were driven to their destinations\n'
              f'Customers left: {", ".join(str(x) for x in customers)}')
        exit(0)

print(f'All customers were driven to their destinations\n'
      f'Total time: {total_time} minutes')
