health = 100
bitcoins = 0

rooms = input().split('|')

best_room = 0

for room in rooms:
    command, amount = room.split()
    best_room += 1
    if command == 'potion':
        health += int(amount)
        if health + int(amount) > 100:
            print(f'You healed for {100 - (health - int(amount))} hp.')
            health = 100
        else:
            print(f'You healed for {amount} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        print(f'You found {amount} bitcoins.')
        bitcoins += int(amount)
    else:
        monster = command
        health -= int(amount)
        if health > 0:
            print(f'You slayed {monster}.')
        else:
            print(f'You died! Killed by {monster}.')
            print(f'Best room: {best_room}')
            exit(0)

print(f'You\'ve made it!')
print(f'Bitcoins: {bitcoins}')
print(f'Health: {health}')
