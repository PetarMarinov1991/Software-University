items = {
    'shards': [0, 'Shadowmourne'],
    'fragments': [0, 'Valanyr'],
    'motes': [0, 'Dragonwrath']
}
junk = dict()

victory = False

while not victory:
    line = input().split()

    for i in range(0, len(line), 2):
        value, item = int(line[i]), (line[i + 1]).lower()

        if item not in junk and item not in items:
            junk.update({item: value})
        elif item in junk:
            junk[item] += value
        elif item in items:
            items[item][0] += value
            if items[item][0] >= 250:
                items[item][0] -= 250
                print(f'{items[item][1]} obtained!')
                victory = True
                break

items = {k: v for k, v in sorted(sorted(items.items()), key=lambda x: -x[1][0])}

print('\n'.join([f'{item}: {value[0]}' for item, value in items.items()]))
print('\n'.join([f'{item}: {value}' for item, value in sorted(junk.items())]))
