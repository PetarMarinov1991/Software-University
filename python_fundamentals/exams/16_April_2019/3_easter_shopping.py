def valid_idx(index, my_list):
    if 0 <= index < len(my_list):
        return True


shops = input().split()
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0]

    if command == 'Include':
        shop = line[1]
        shops.append(shop)
    elif command == 'Visit':
        first_or_last, num_of_shops = line[1], int(line[2])
        if not num_of_shops > len(shops):
            if first_or_last == 'first':
                shops = shops[num_of_shops:]
            elif first_or_last == 'last':
                shops = shops[:-num_of_shops]
    elif command == 'Prefer':
        idx_1, idx_2 = int(line[1]), int(line[2])
        if valid_idx(idx_1, shops) and valid_idx(idx_2, shops):
            shops[idx_1], shops[idx_2] = shops[idx_2], shops[idx_1]
    elif command == 'Place':
        shop, idx = line[1], int(line[2])
        if valid_idx(idx + 1, shops):
            shops.insert(idx + 1, shop)

print('Shops left:')
print(' '.join([shop for shop in shops]))
