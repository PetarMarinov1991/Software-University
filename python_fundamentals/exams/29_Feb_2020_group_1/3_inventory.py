items = input().split(', ')

while True:
    line = input().split(' - ')
    command = line[0]

    if command == 'Craft!':
        break

    item = line[1]
    if command == 'Collect':
        if item not in items:
            items.append(item)
    elif command == 'Drop':
        if item in items:
            items.remove(item)
    elif command == 'Combine Items':
        old_item, new_item = item.split(':')
        if old_item in items:
            items.insert(items.index(old_item) + 1, new_item)
    elif command == 'Renew':
        if item in items:
            items.remove(item)
            items.append(item)

print(', '.join([item for item in items]))
