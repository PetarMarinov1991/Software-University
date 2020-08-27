data = input().split('|')
budget = float(input())

new_prices = []

for value in data:
    value = value.split('->')
    item, price = value[0], float(value[1])

    valid = False

    case_1 = item == 'Clothes' and price <= 50
    case_2 = item == 'Shoes' and price <= 35
    case_3 = item == 'Accessories' and price <= 20.50

    if case_1 or case_2 or case_3:
        valid = True

    if valid and budget >= price:
        budget -= price
        new_prices.append(f'{price * 1.4:.2f}')

print(f'{" ".join([price for price in new_prices])}')
profit = sum(map(float, new_prices))
print(f'Profit: {profit - profit / 1.4:.2f}')

if profit + budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
