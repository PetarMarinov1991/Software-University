def find_miner(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 's':
                return i, j


def valid_moves(matrix, steps):
    miner_pos = find_miner(matrix)
    directions = {
        'up': [-1, 0],
        'right': [0, 1],
        'left': [0, -1],
        'down': [1, 0]
    }
    completed_moves = []
    for step in steps:
        row = miner_pos[0] + directions[step][0]
        col = miner_pos[1] + directions[step][1]
        if row in range(len(matrix)) and col in range(len(matrix)):
            miner_pos = [row, col]
            completed_moves.append(miner_pos)
    return completed_moves


def collect_coals(matrix, steps):
    coals_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'c':
                coals_count += 1
    coals_collected = 0
    current_pos = [0, 0]
    for step in steps:
        current_pos = [step[0], step[1]]
        if matrix[current_pos[0]][current_pos[1]] == 'c':
            matrix[current_pos[0]][current_pos[1]] = '*'
            coals_collected += 1
            if coals_collected == coals_count:
                return f'You collected all coals! {current_pos[0], current_pos[1]}'
        elif matrix[current_pos[0]][current_pos[1]] == 'e':
            return f'Game over! {current_pos[0], current_pos[1]}'
    return f'{coals_count - coals_collected} coals left. {current_pos[0], current_pos[1]}'


n = int(input())
moves = input().split()
playground = [[x for x in input().split()] for _ in range(n)]

print(collect_coals(playground, valid_moves(playground, moves)))
