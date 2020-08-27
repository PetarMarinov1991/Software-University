heroes = dict()

for _ in range(int(input())):
    line = input().split()

    hero, hp, mp = line[0], int(line[1]), int(line[2])
    heroes[hero] = [hp, mp]

    if heroes[hero][0] > 100:
        heroes[hero][0] = 100
    if heroes[hero][1] > 200:
        heroes[hero][1] = 200

while True:
    line = input().split(' - ')
    command = line[0]

    if command == 'End':
        break

    hero = line[1]
    if command == 'CastSpell':
        mp_needed, spell = int(line[2]), line[3]
        if hero in heroes:
            if mp_needed <= heroes[hero][1]:
                heroes[hero][1] -= mp_needed
                print(f'{hero} has successfully cast {spell} and now has {heroes[hero][1]} MP!')
            else:
                print(f'{hero} does not have enough MP to cast {spell}!')
    elif command == 'TakeDamage':
        dmg, attacker = int(line[2]), line[3]
        if hero in heroes:
            heroes[hero][0] -= dmg
            if heroes[hero][0] > 0:
                print(f'{hero} was hit for {dmg} HP by {attacker} and now has {heroes[hero][0]} HP left!')
            else:
                print(f'{hero} has been killed by {attacker}!')
                del heroes[hero]
    elif command == 'Recharge':
        amount = int(line[2])
        if hero in heroes:
            heroes[hero][1] += amount
            if heroes[hero][1] > 200:
                print(f'{hero} recharged for {200 - (heroes[hero][1] - amount)} MP!')
                heroes[hero][1] = 200
            else:
                print(f'{hero} recharged for {amount} MP!')
    elif command == 'Heal':
        amount = int(line[2])
        if hero in heroes:
            heroes[hero][0] += amount
            if heroes[hero][0] > 100:
                print(f'{hero} healed for {100 - (heroes[hero][0] - amount)} HP!')
                heroes[hero][0] = 100
            else:
                print(f'{hero} healed for {amount} HP!')

heroes = {k: v for k, v in sorted(heroes.items(), key=lambda x: (-x[1][0], x[0]))}

for hero, value in heroes.items():
    print(hero)
    print(f'HP: {value[0]}')
    print(f'MP: {value[1]}')
