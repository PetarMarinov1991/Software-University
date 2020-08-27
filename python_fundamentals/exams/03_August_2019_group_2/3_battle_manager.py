people = dict()

while True:
    line = input().split(':')
    command = line[0]

    if command == 'Results':
        break

    if command == 'Add':
        name, health, energy = line[1], int(line[2]), int(line[3])
        if name not in people:
            people[name] = [0, 0]
        people[name][0] += health
        people[name][1] += energy
    elif command == 'Attack':
        attacker, defender, dmg = line[1], line[2], int(line[3])
        if attacker in people and defender in people:
            people[defender][0] -= dmg
            if people[defender][0] <= 0:
                print(f'{defender} was disqualified!')
                del people[defender]
            people[attacker][1] -= 1
            if people[attacker][1] <= 0:
                print(f'{attacker} was disqualified!')
                del people[attacker]
    elif command == 'Delete':
        name = line[1]
        if name == 'All':
            people.clear()
        elif name in people:
            del people[name]

print(f'People count: {len(people)}')
people = {k: v for k, v in sorted(people.items(), key=lambda x: (-x[1][0], x[0]))}
for person, stats in people.items():
    health, energy = stats
    print(f'{person} - {health} - {energy}')
