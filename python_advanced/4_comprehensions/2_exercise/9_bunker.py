categories = input().split(', ')
categories_dict = dict()

for _ in range(int(input())):
    data = [i.split(';') for i in input().split(' - ')]
    category, item = data[0][0], data[1][0]
    quantity = int(data[2][0].split(':')[1])
    quality = int(data[2][1].split(':')[1])

    if category not in categories_dict:
        categories_dict[category] = [[], 0, 0]
    if item not in categories_dict[category]:
        categories_dict[category][0].append(item)
    categories_dict[category][1] += quantity
    categories_dict[category][2] += quality

print(f'Count of items: {sum([y[1] for x, y in categories_dict.items()])}')
print(f'Average quality: {(sum(y[2] for x, y in categories_dict.items())) / len(categories_dict):.2f}')
print('\n'.join([f'{x} -> {", ".join([x for x in y[0]])}' for x, y in categories_dict.items()]))
