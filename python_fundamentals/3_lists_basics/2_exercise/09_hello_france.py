items = input().split('|')
budget = float(input())

allowed_items = {
    'Clothes': 50.00,
    'Shoes': 35.00,
    'Accessories': 20.50
}

profit = budget
items_bought = []

for i in items:
    args = i.split('->')
    item, price = args[0], float(args[1])

    if price <= allowed_items[item] and price <= budget:
        budget -= price
        items_bought.append(price * 1.4)

budget += sum(items_bought)
profit = budget - profit

print(f'{" ".join([f"{item:.2f}" for item in items_bought])}')
print(f'Profit: {profit:.2f}')

if budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
