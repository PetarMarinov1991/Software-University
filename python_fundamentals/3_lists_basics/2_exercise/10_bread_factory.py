events = input().split('|')

energy = 100
coins = 100
day_completed = True

for e in events:
    args = e.split('-')
    event, num = args[0], int(args[1])

    if event == 'rest':
        gained_energy = 0

        if energy + num > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            energy += num
            gained_energy = num

        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')

    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += num
            print(f'You earned {num} coins.')
        else:
            energy += 50
            print('You had to rest!')

    else:
        if coins >= num:
            coins -= num
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            day_completed = False
            break

if day_completed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
