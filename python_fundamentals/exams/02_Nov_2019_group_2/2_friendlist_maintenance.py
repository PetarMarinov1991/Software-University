names = input().split(', ')

while True:
    line = input().split()
    command = line[0]

    if command == 'Report':
        break

    if command == 'Blacklist':
        name = line[1]
        if name not in names:
            print(f'{name} was not found.')
        else:
            print(f'{name} was blacklisted.')
            idx = names.index(name)
            names[idx] = 'Blacklisted'
    elif command == 'Error':
        idx = int(line[1])
        if names[idx] not in ['Blacklisted', 'Lost']:
            print(f'{names[idx]} was lost due to an error.')
            names[idx] = 'Lost'
    elif command == 'Change':
        idx, new_name = int(line[1]), line[2]
        if 0 <= idx < len(names):
            print(f'{names[idx]} changed his username to {new_name}.')
            names[idx] = new_name

print(f'Blacklisted names: {names.count("Blacklisted")}')
print(f'Lost names: {names.count("Lost")}')
print(f'{" ".join([name for name in names])}')
