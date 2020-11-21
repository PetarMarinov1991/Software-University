points = int(input())

moves = 0

while points > 0:
    moves += 1
    target_sector = input()

    if target_sector == 'bullseye':
        print(f'Congratulations! You won the game with a bullseye in {moves} moves!')
        break

    points_count = int(input())

    if target_sector == 'triple ring':
        points -= points_count * 3
    elif target_sector == 'double ring':
        points -= points_count * 2
    elif target_sector == 'number section':
        points -= points_count

    if points < 0:
        print(f'Sorry, you lost. Score difference: {abs(points)}.')
    elif points == 0:
        print(f'Congratulations! You won the game in {moves} moves!')

