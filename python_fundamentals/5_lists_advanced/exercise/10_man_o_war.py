def valid_idx(index, my_list):
    if 0 <= index < len(my_list):
        return True


pirate_ship = list(map(int, input().split('>')))
war_ship = list(map(int, input().split('>')))
max_health = int(input())

stalemate = True

while True:
    line = input()

    if line == 'Retire':
        break

    if line == 'Status':
        count = 0
        for section in pirate_ship:
            if section < 0.2 * max_health:
                count += 1
        print(f'{count} sections need repair.')

    line = line.split()
    command = line[0]

    if command == 'Fire':
        idx, dmg = int(line[1]), int(line[2])
        if valid_idx(idx, war_ship):
            war_ship[idx] -= dmg
            if war_ship[idx] <= 0:
                print('You won! The enemy ship has sunken.')
                stalemate = False
                break
    elif command == 'Defend':
        start_idx, end_idx, dmg = int(line[1]), int(line[2]), int(line[3])
        if valid_idx(start_idx, pirate_ship) and valid_idx(end_idx, pirate_ship):
            for section in range(start_idx, end_idx + 1):
                pirate_ship[section] -= dmg
                if pirate_ship[section] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    stalemate = False
                    break
    elif command == 'Repair':
        idx, health = int(line[1]), int(line[2])
        if valid_idx(idx, pirate_ship):
            pirate_ship[idx] += health
            if pirate_ship[idx] >= max_health:
                pirate_ship[idx] = max_health

if stalemate:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(war_ship)}')
