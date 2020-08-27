store = dict()

while True:
    line = input().split()

    if line[0] == 'buy':
        break

    product, price, quantity = line[0], float(line[1]), int(line[2])

    if product not in store:
        store.update({product: [price, quantity]})
    else:
        store[product][0] = price
        store[product][1] += quantity

for product, value in store.items():
    print(f'{product} -> {value[0] * value[1]:.2f}')
