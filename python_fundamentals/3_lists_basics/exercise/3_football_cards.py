cards = input().split()

team_A = list(range(1, 12))
team_B = list(range(1, 12))
bench_team_A = []
bench_team_B = []

for card in cards:
    arg = card.split('-')
    team = arg[0]
    player = int(arg[1])

    if team == 'A':
        if player in bench_team_A:
            continue
        team_A.remove(player)
        bench_team_A.append(player)

    elif team == 'B':
        if player in bench_team_B:
            continue
        team_B.remove(player)
        bench_team_B.append(player)

print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')

if len(bench_team_A) > 4 or len(bench_team_B) > 4:
    print('Game was terminated')
