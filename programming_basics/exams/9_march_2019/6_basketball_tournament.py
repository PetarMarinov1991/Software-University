import math

desi_team_wins = 0
enemy_team_wins = 0
total_games = 0

command = input()

while command != 'End of tournaments':
    tournament_name = command

    games = int(input())

    for number in range(1, games + 1):
        desi_team_points = int(input())
        enemy_team_points = int(input())
        total_games += 1

        if desi_team_points > enemy_team_points:
            desi_team_wins += 1
            print(f'Game {number} of tournament {tournament_name}: win with {desi_team_points - enemy_team_points} points.')

        elif enemy_team_points > desi_team_points:
            enemy_team_wins += 1
            print(f'Game {number} of tournament {tournament_name}: lost with {enemy_team_points - desi_team_points} points.')

    command = input()

    if command == 'End of tournaments':
        percentage_won_games = (desi_team_wins / total_games) * 100
        percentage_lost_games = (enemy_team_wins / total_games) * 100
        print(f'{percentage_won_games:.2f}% matches win')
        print(f'{percentage_lost_games:.2f}% matches lost')
        break
