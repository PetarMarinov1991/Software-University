groceries = input().split('!')

while True:
    line = input()

    if line == 'Go Shopping!':
        break

    line = line.split()
    command, product = line[0], line[1]

    if command == 'Urgent':
        if product not in groceries:
            groceries.insert(0, product)
    elif command == 'Unnecessary':
        if product in groceries:
            groceries.remove(product)
    elif command == 'Correct':
        new_product = line[2]
        if product in groceries:
            groceries.insert(groceries.index(product), new_product)
            groceries.remove(product)
    elif command == 'Rearrange':
        if product in groceries:
            groceries.remove(product)
            groceries.append(product)

print(', '.join([product for product in groceries]))
