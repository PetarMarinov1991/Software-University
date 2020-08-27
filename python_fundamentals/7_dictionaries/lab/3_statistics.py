bakery = dict()

while True:
    command = input().split(':')

    if command[0] == 'statistics':
        break

    product, value = command[0], int(command[1])

    if product not in bakery:
        bakery.update({product: value})
    else:
        bakery[product] += value

print('Products in stock:')
for (product, value) in bakery.items():
    print(f'- {product}: {value}')
print(f'Total Products: {len(bakery.keys())}')
print(f'Total Quantity: {sum(bakery.values())}')
