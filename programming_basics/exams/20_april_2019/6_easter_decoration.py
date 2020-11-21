customers = int(input())

total_sum = 0
customer_sum = 0
items = 0

for i in range(customers):
    customer_sum = 0
    items = 0
    command = input()

    while command != 'Finish':
        purchase = command
        items += 1

        if purchase == 'basket':
            customer_sum += 1.50
            total_sum += 1.50
        elif purchase == 'wreath':
            customer_sum += 3.80
            total_sum += 3.80
        elif purchase == 'chocolate bunny':
            customer_sum += 7
            total_sum += 7

        command = input()

        if command == 'Finish':
            if items % 2 == 0:
                diff = customer_sum * 0.2
                customer_sum *= 0.8
                total_sum -= diff
            print(f'You purchased {items} items for {customer_sum:.2f} leva.')
            break

average_sum = total_sum / customers

print(f'Average bill per client is: {average_sum:.2f} leva.')
