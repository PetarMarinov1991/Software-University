player_one_eggs = int(input())
player_two_eggs = int(input())

player_one_out_of_eggs = False
player_two_out_of_eggs = False

command = input()

while command != 'End of battle':
    if command == 'one':
        player_two_eggs -= 1
    elif command == 'two':
        player_one_eggs -= 1

    if player_one_eggs == 0:
        player_one_out_of_eggs = True
    elif player_two_eggs == 0:
        player_two_out_of_eggs = True

    if player_one_out_of_eggs:
        print(f'Player one is out of eggs. Player two has {player_two_eggs} eggs left.')
        break
    elif player_two_out_of_eggs:
        print(f'Player two is out of eggs. Player one has {player_one_eggs} eggs left.')
        break

    command = input()

    if command == 'End of battle':
        print(f'Player one has {player_one_eggs} eggs left.')
        print(f'Player two has {player_two_eggs} eggs left.')
        break
