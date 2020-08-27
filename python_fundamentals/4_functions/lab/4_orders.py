def product_price(product):
    products = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00
    }
    return products.__getitem__(product)


def calculate_price_for_quantity(product, quantity):
    return f'{product_price(product) * quantity:.2f}'


print(calculate_price_for_quantity(product=input(), quantity=int(input())))
