budget = float(input())

products_count = 0
products_total_price = 0

command = input()

while command != 'Stop':
    product = command
    product_price = float(input())

    products_count += 1

    if products_count % 3 == 0:
        products_total_price += product_price / 2
        product_price -= product_price / 2
    else:
        products_total_price += product_price

    if product_price > budget:
        diff = abs(product_price - budget)
        print('You don\'t have enough money!')
        print(f'You need {diff:.2f} leva!')
        break

    budget -= product_price

    command = input()

    if command == 'Stop':
        print(f'You bought {products_count} products for {products_total_price:.2f} leva.')

