quantity = int(input())
days = int(input())

ornament_set_count = 0
tree_skirt_count = 0
tree_garlands_count = 0
tree_lights_count = 0

days_count = 0
christmas_spirit = 0

while days > days_count:
    days_count += 1

    if days_count % 11 == 0:
        quantity += 2

    if days_count % 2 == 0:
        ornament_set_count += quantity
        christmas_spirit += 5

    if days_count % 3 == 0:
        tree_skirt_count += quantity
        tree_garlands_count += quantity
        christmas_spirit += 13

    if days_count % 5 == 0:
        tree_lights_count += quantity
        christmas_spirit += 17
        if days_count % 3 == 0:
            christmas_spirit += 30

    if days_count % 10 == 0:
        tree_skirt_count += 1
        tree_garlands_count += 1
        tree_lights_count += 1
        christmas_spirit -= 20

if days % 10 == 0:
    christmas_spirit -= 30

total_cost = ornament_set_count * 2 + tree_skirt_count * 5 + tree_garlands_count * 3 + tree_lights_count * 15

print(f'Total cost: {total_cost}')
print(f'Total spirit: {christmas_spirit}')
