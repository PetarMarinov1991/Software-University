games_count = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0
all_games = 0

for games in range(games_count):
    game_name = input()
    all_games += 1

    if game_name == 'Hearthstone':
        hearthstone += 1
    elif game_name == 'Fornite':
        fornite += 1
    elif game_name == 'Overwatch':
        overwatch += 1
    else:
        others += 1

hearthstone_percentage = (hearthstone / all_games) * 100
fornite_percentage = (fornite / all_games) * 100
overwatch_percentage = (overwatch / all_games) * 100
others_percentage = (others / all_games) * 100

print(f'Hearthstone - {hearthstone_percentage:.2f}%')
print(f'Fornite - {fornite_percentage:.2f}%')
print(f'Overwatch - {overwatch_percentage:.2f}%')
print(f'Others - {others_percentage:.2f}%')
