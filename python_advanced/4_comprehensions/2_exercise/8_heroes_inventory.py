heroes_dict = {h: [] for h in input().split(', ')}

while True:
    line = input().split('-')

    if line[0] == 'End':
        break

    name, item, cost = line[0], line[1], line[2]
    if item not in heroes_dict[name]:
        heroes_dict[name].append(item)
        heroes_dict[name].append(cost)

for name, value in heroes_dict.items():
    items_count = 0
    cost = 0
    for i in value:
        if i.isdigit():
            cost += int(i)
        else:
            items_count += 1
    print(f'{name} -> Items: {items_count}, Cost: {cost}')
