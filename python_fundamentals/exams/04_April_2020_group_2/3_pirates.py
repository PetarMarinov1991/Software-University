towns = dict()

while True:
    line = input().split('||')
    command = line[0]

    if command == 'Sail':
        break

    town, population, gold = line[0], int(line[1]), int(line[2])
    if town not in towns:
        towns[town] = [0, 0]
    towns[town][0] += population
    towns[town][1] += gold

while True:
    line = input().split('=>')
    command = line[0]

    if command == 'End':
        break

    if command == 'Plunder':
        town, population, gold = line[1], int(line[2]), int(line[3])
        towns[town][0] -= population
        towns[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {population} citizens killed.')
        if towns[town][0] <= 0 or towns[town][1] <= 0:
            print(f'{town} has been wiped off the map!')
            del towns[town]

    elif command == 'Prosper':
        town, gold = line[1], int(line[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            towns[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {towns[town][1]} gold.')

towns = {k: v for k, v in sorted(towns.items(), key=lambda x: (-x[1][1], x[0]))}

if towns:
    print(f'Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:')
    for town, value in towns.items():
        print(f'{town} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
