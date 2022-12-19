def calc_order_price(product, quantity):
    products = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00
    }

    return f'{products[product] * quantity:.2f}'


product = input()
quantity = int(input())
print(calc_order_price(product, quantity))
