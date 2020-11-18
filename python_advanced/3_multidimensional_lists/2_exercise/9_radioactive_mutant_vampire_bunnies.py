def find_player(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'P':
                return i, j


def valid_range(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix[row]))


def mutate_bunnies(matrix, steps):
    player_pos = find_player(matrix)
    directions = {
        'U': [-1, 0],
        'L': [0, -1],
        'R': [0, 1],
        'D': [1, 0]
    }
    for step in range(len(steps)):
        move = steps[step]
        new_matrix = [['.' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'B':
                    new_matrix[i][j] = 'B'
                    for _, value in directions.items():
                        step = [i + value[0], j + value[1]]
                        if valid_range(step[0], step[1], matrix):
                            if new_matrix[step[0]][step[1]] == '.':
                                new_matrix[step[0]][step[1]] = 'B'
        player_move = [player_pos[0] + directions[move][0], player_pos[1] + directions[move][1]]
        matrix_output = '\n'.join([''.join([str(x) for x in new_matrix[i]]) for i in range(len(new_matrix))])
        if valid_range(player_move[0], player_move[1], matrix):
            if new_matrix[player_move[0]][player_move[1]] == 'B':
                return matrix_output + f'\ndead: {player_move[0]} {player_move[1]}'
            else:
                new_matrix[player_move[0]][player_move[1]] = 'P'
                player_pos = player_move
                matrix = new_matrix
        else:
            return matrix_output + f'\nwon: {player_pos[0]} {player_pos[1]}'


playground = [[x for x in input()] for _ in range([int(x) for x in input().split()][0])]
print(mutate_bunnies(playground, input()))
