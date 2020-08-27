stores = dict()

while True:
    info = input().split('->')
    command = info[0]

    if command == 'END':
        break

    store = info[1]

    if command == 'Add':
        items = info[2].split(',')
        if store not in stores:
            stores.update({store: [item for item in items]})
        else:
            stores[store] += [item for item in items]
    elif command == 'Remove':
        if store in stores:
            del stores[store]

stores = {k: v for k, v in sorted(sorted(stores.items(), reverse=True), key=lambda x: -len(x[1]))}

print('Stores list:')
for store, items in stores.items():
    print(f'{store}\n' + '\n'.join([f'<<{item}>>' for item in items]))
