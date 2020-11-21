player_one = input()
player_two = input()

winner_is_found = False
winner = ''
winner_points = 0
player_one_points = 0
player_two_points = 0

command = input()

while command != 'End of game':

    card_player_one = int(command)
    card_player_two = int(input())

    while card_player_one == card_player_two:
        print('Number wars!')

        card_player_one = int(input())
        card_player_two = int(input())

        if card_player_one > card_player_two:
            winner = player_one
            winner_points = player_one_points
            winner_is_found = True

        elif card_player_two > card_player_one:
            winner = player_two
            winner_points = player_two_points
            winner_is_found = True

    if winner_is_found:
        print(f'{winner} is winner with {winner_points} points')
        break

    if card_player_one > card_player_two:
        player_one_points += card_player_one - card_player_two
        winner_points = player_one_points
    else:
        player_two_points += card_player_two - card_player_one
        winner_points = player_two_points

    command = input()

    if command == 'End of game':
        print(f'{player_one} has {player_one_points} points')
        print(f'{player_two} has {player_two_points} points')
        break
