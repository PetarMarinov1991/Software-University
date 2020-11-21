from math import floor as fl

tournaments = int(input())
rank_list_starting_points = int(input())

points_won = 0
tournaments_won = 0

for parts in range(tournaments):
    stage = input()

    if stage == 'W':
        points_won += 2000
        tournaments_won += 1

    elif stage == 'F':
        points_won += 1200

    elif stage == 'SF':
        points_won += 720

average_points = points_won / tournaments
percentage_tournaments_won = (tournaments_won / tournaments) * 100

print(f'Final points: {points_won + rank_list_starting_points}')
print(f'Average points: {fl(average_points)}')
print(f'{percentage_tournaments_won:.2f}%')
