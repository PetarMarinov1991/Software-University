heroes = dict()

while True:
    line = input()

    if line == 'End':
        break

    line = line.split()
    command, hero = line[0], line[1]

    if command == 'Enroll':
        if hero not in heroes:
            heroes.update({hero: []})
        else:
            print(f'{hero} is already enrolled.')
    elif command == 'Learn':
        spell = line[2]
        if hero not in heroes:
            print(f'{hero} doesn\'t exist.')
        else:
            if spell in heroes[hero]:
                print(f'{hero} has already learnt {spell}.')
            else:
                heroes[hero].append(spell)
    elif command == 'Unlearn':
        spell = line[2]
        if hero not in heroes:
            print(f'{hero} doesn\'t exist.')
        else:
            if spell not in heroes[hero]:
                print(f'{hero} doesn\'t know {spell}.')
            else:
                heroes[hero].remove(spell)

heroes = {k: v for k, v in sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0]))}

print('Heroes:')
for hero, spell in heroes.items():
    print(f'== {hero}: {", ".join([x for x in spell])}')
