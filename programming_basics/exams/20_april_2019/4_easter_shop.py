starting_eggs = int(input())

command = input()
sold_eggs = 0

while command != 'Close':
    if command == 'Buy':
        bought_eggs = int(input())

        if bought_eggs > starting_eggs:
            print('Not enough eggs in store!')
            print(f'You can buy only {starting_eggs}.')
            break

        starting_eggs -= bought_eggs
        sold_eggs += bought_eggs

    elif command == 'Fill':
        filled_eggs = int(input())
        starting_eggs += filled_eggs

    command = input()

    if command == 'Close':
        print('Store is closed!')
        print(f'{sold_eggs} eggs sold.')
        break
