from collections import deque


def check_bombs(bombs):
    return bombs[40][1] >= 3 and bombs[60][1] >= 3 and bombs[120][1] >= 3


def output_collection(collection):
    if not collection:
        return 'empty'
    return ', '.join([str(x) for x in collection])


def bombs_output(bombs):
    result = []
    for key, value in bombs.items():
        result.append(f'{value[0]}: {value[1]}')
    return '\n'.join(result)


bomb_effect, bomb_casing = [deque([int(x) for x in input().split(', ')]) for _ in range(2)]

bombs_dict = {
    60: ['Cherry Bombs', 0],
    40: ['Datura Bombs', 0],
    120: ['Smoke Decoy Bombs', 0]
}

while bomb_effect and bomb_casing:
    current_bomb_effect = bomb_effect[0]
    current_bomb_casing = bomb_casing[-1]

    if current_bomb_effect + current_bomb_casing in bombs_dict.keys():
        bombs_dict[current_bomb_effect + current_bomb_casing][1] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5

    if check_bombs(bombs_dict):
        print('Bene! You have successfully filled the bomb pouch!')
        break

if not check_bombs(bombs_dict):
    print('You don\'t have enough materials to fill the bomb pouch.')

print('Bomb Effects: ' + output_collection(bomb_effect))
print('Bomb Casings: ' + output_collection(bomb_casing))
print(bombs_output(bombs_dict))
