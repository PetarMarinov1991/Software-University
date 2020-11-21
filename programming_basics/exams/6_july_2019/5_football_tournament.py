team_name = input()
matches_payed = int(input())

if matches_payed == 0:
    print(f'{team_name} hasn\'t played any games during this season.')
    exit(0)

wins = 0
draws = 0
loses = 0
points = 0

for matches in range(matches_payed):
    result = input()

    if result == 'W':
        wins += 1
        points += 3
    elif result == 'D':
        draws += 1
        points += 1
    elif result == 'L':
        loses += 1

win_percentage = wins / matches_payed * 100

print(f'{team_name} has won {points} points during this season.')
print('Total stats:')
print(f'## W: {wins}')
print(f'## D: {draws}')
print(f'## L: {loses}')
print(f'Win rate: {win_percentage:.2f}%')

