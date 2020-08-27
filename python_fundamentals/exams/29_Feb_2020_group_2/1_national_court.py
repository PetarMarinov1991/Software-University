employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
customers = int(input())

serviced_customers = employee_1 + employee_2 + employee_3
hours = 0

while customers > 0:
    customers -= serviced_customers
    hours += 1

    if hours % 4 == 0:
        hours += 1
        continue

print(f'Time needed: {hours}h.')
