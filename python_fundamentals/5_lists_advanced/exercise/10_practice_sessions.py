roads = dict()

while True:
    info = input().split('->')
    command = info[0]

    if command == 'END':
        break

    road = info[1]
    if command == 'Add':
        racer = info[2]
        if road not in roads:
            roads.update({road: [racer]})
        else:
            roads[road] += [racer]
    elif command == 'Move':
        racer, next_road = info[2], info[3]
        if racer in roads[road]:
            roads[road].remove(racer)
            roads[next_road] += [racer]
    elif command == 'Close':
        if road in roads:
            del roads[road]

roads = {k: v for k, v in sorted(sorted(roads.items()), key=lambda x: len(x[1]), reverse=True)}

print('Practice sessions:')
for road, racers in roads.items():
    print(road)
    for racer in racers:
        print(f'++{racer}')
