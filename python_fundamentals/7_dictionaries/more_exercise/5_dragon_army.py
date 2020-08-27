dragons = dict()

for _ in range(int(input())):
    color, name, dmg, hp, armor = input().split()

    if dmg == 'null':
        dmg = 45
    if hp == 'null':
        hp = 250
    if armor == 'null':
        armor = 10

    if color not in dragons:
        dragons.update({color: {name: [int(dmg), int(hp), int(armor)]}})
    else:
        dragons[color].update({name: [int(dmg), int(hp), int(armor)]})

for color, info in dragons.items():
    avg_dmg, avg_health, avg_armor = 0, 0, 0
    i = 0
    for name, stats in sorted(info.items()):
        avg_dmg += stats[0]
        avg_health += stats[1]
        avg_armor += stats[2]
        i += 1
    avg_dmg /= i
    avg_health /= i
    avg_armor /= i
    print(f'{color}::({avg_dmg:.2f}/{avg_health:.2f}/{avg_armor:.2f})')
    for name, stats in sorted(info.items()):
        print(f'-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}')
