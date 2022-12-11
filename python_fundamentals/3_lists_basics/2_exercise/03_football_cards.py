team_A = list(range(1, 12))
team_B = list(range(1, 12))

card = input().split()

game_is_terminated = False

for info in card:
    team, player = info.split('-')
    player_number = int(player)

    if team == 'A':
        if player_number in team_A:
            team_A.remove(player_number)
    elif team == 'B':
        if player_number in team_B:
            team_B.remove(player_number)

    if len(team_A) < 7 or len(team_B) < 7:
        game_is_terminated = True
        break

print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')
if game_is_terminated:
    print('Game was terminated')
