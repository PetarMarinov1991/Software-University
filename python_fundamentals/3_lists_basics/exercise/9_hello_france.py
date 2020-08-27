string = input().split('|')
budget = float(input())

items_bought = []

for command in string:
    arg = command.split('->')
    item = arg[0]
    item_price = float(arg[1])

    if item == 'Clothes' and item_price <= 50.00:
        if budget - item_price >= 0:
            items_bought.append(item_price * 1.4)
            budget -= item_price
    elif item == 'Shoes' and item_price <= 35.00:
        if budget - item_price >= 0:
            items_bought.append(item_price * 1.4)
            budget -= item_price
    elif item == 'Accessories' and item_price <= 20.50:
        if budget - item_price >= 0:
            items_bought.append(item_price * 1.4)
            budget -= item_price

profit = sum(items_bought) - (sum(items_bought) / 1.4)
budget += sum(items_bought)

for item in items_bought:
    print(f'{item:.2f}', end=' ')
print(f'\nProfit: {profit:.2f}')

if budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
