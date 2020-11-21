trip_days = int(input())

day_balance = 60
products_bought = 0

for days in range(1, trip_days + 1):

    while day_balance > 0:
        command = input()

        if command == 'Day over':
            print(f'Money left from today: {day_balance:.2f}. You\'ve bought {products_bought} products. ')
            day_balance += 60
            products_bought = 0
            break

        product_price = float(command)

        if product_price > day_balance:
            continue

        else:
            day_balance -= product_price
            products_bought += 1

            if day_balance == 0:
                day_balance += 60
                print(f'Daily limit exceeded! You\'ve bought {products_bought} products.')
                products_bought = 0
                break
