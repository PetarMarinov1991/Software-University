def find_player(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'P':
                return i, j


def valid_move(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix[row]))


def player_moves(matrix):
    player_pos = find_player(matrix)
    directions = {
        'up': [-1, 0],
        'left': [0, -1],
        'right': [0, 1],
        'down': [1, 0]
    }
    for _ in range(int(input())):
        direction = input()
        current_pos = directions[direction][0] + player_pos[0], directions[direction][1] + player_pos[1]
        if valid_move(current_pos[0], current_pos[1], matrix):
            current_char = matrix[current_pos[0]][current_pos[1]]
            if current_char.isalpha():
                string_as_list.append(current_char)
            matrix[player_pos[0]][player_pos[1]] = '-'
            matrix[current_pos[0]][current_pos[1]] = 'P'
            player_pos = current_pos[0], current_pos[1]
        else:
            if string_as_list:
                string_as_list.pop()
    return matrix


def output(string, matrix):
    matrix = player_moves(matrix)
    return f'{"".join([x for x in string])}\n' + \
           '\n'.join([''.join([str(x) for x in matrix[i]]) for i in range(len(matrix))])


string_as_list = [x for x in input()]
field = [[x for x in input()] for _ in range(int(input()))]

print(output(string_as_list, field))
