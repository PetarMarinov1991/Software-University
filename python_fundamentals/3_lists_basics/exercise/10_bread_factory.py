string = input().split('|')
coins = 100
energy = 100

for command in string:
    arg = command.split('-')
    command = arg[0]
    add_energy = int(arg[1])

    if command == 'rest':
        if energy + add_energy <= 100:
            energy += add_energy
            print(f'You gained {add_energy} energy.')
        else:
            print('You gained 0 energy.')
        print(f'Current energy: {energy}.')

    elif command == 'order':
        if energy - 30 < 0:
            energy += 50
            print('You had to rest!')
        else:
            energy -= 30
            new_coins = add_energy
            coins += new_coins
            print(f'You earned {new_coins} coins.')

    else:
        if coins - add_energy > 0:
            coins -= add_energy
            print(f'You bought {command}.')
        else:
            print(f'Closed! Cannot afford {command}.')
            exit(0)

print('Day completed!')
print(f'Coins: {coins}')
print(f'Energy: {energy}')
