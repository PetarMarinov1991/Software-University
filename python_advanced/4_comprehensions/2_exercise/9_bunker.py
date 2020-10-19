categories = {n: [] for n in input().split(', ')}

items_count = 0
total_quality = 0

for _ in range(int(input())):
    line = input().split(' - ')
    category, kind, quality_and_quantity = line[0], line[1], line[2]
    quantity, quality = quality_and_quantity.split(';')
    quality = quality.split(':')
    quantity = quantity.split(':')
    if kind not in categories[category]:
        categories[category].append(kind)
        items_count += int(quantity[1])
        total_quality += int(quality[1])

print(f'Count of items: {items_count}')
print(f'Average quality: {total_quality / len(categories.keys()):.2f}')
for food, kind in categories.items():
    print(f'{food} -> {", ".join(kind)}')
