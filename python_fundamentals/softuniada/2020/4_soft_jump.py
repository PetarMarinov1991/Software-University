def shift_step(my_list, shift=0):
    length = len(my_list)
    for idx, elem in enumerate(my_list[:]):
        my_list[(idx + shift) % length] = elem
    return my_list


data = list(map(int, input().split()))
rows, cols = data[0], data[1]

game = []
for _ in range(rows):
    current_row = input()
    row = []
    for char in current_row:
        row.append(char)
    game.append(row)

steps = int(input())
for step in range(steps):
    info = input().split()
    arr, pos = int(info[0]), int(info[1])
    game[arr] = shift_step(game[arr], pos)

jumps = 0
player_idx = 0

for r in range(len(game), 0, -1):
    player, step = 'S', '-'
    for e in game[r - 1]:
        if e == player:
            player_idx = game[r - 1].index(player)
        if e == step:
            step_idx = game[r - 1].index(step)
            if game[step_idx] == game[player_idx]:
                if game[r][player_idx] == player and game[r - 1][player_idx] == step:
                    if r == rows - 1:
                        game[r][step_idx] = '0'
                    else:
                        game[r][step_idx] = e
                    game[r - 1].remove(e)
                    game[r - 1].insert(step_idx, player)
                    jumps += 1

if jumps == rows - 1:
    print('Win')
else:
    print('Lose')
print(f'Total Jumps: {jumps}')
for games in game:
    print(''.join(games))
