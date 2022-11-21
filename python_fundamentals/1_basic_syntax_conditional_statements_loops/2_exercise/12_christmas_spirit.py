decor_quantity = int(input())
days_until_xmas = int(input())

total_cost = 0
xmas_spirit = 0

for day in range(1, days_until_xmas + 1):
    if day % 11 == 0:
        decor_quantity += 2
    if day % 2 == 0:
        total_cost += 2 * decor_quantity
        xmas_spirit += 5
    if day % 3 == 0:
        total_cost += (5 + 3) * decor_quantity
        xmas_spirit += 13
    if day % 5 == 0:
        total_cost += 15 * decor_quantity
        xmas_spirit += 17
        if day % 3 == 0:
            xmas_spirit += 30
    if day % 10 == 0:
        total_cost += 23
        xmas_spirit -= 20

if days_until_xmas % 10 == 0:
    xmas_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {xmas_spirit}')
