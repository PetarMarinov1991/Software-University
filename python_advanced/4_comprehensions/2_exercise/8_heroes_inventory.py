names = input().split(', ')

heroes = dict()

while True:
    line = input().split('-')

    if line[0] == 'End':
        break

    name, item, value = line[0], line[1], int(line[2])
    if name not in heroes:
        heroes[name] = [[], 0]
    if item not in heroes[name][0]:
        heroes[name][0].append(item)
        heroes[name][1] += value

print('\n'.join([f'{name} -> Items: {len(value[0])}, Cost: {value[1]}' for name, value in heroes.items()]))
