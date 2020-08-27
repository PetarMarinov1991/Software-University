def find_santa(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                return i, j


def valid_move(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix[row]))


def nice_kids(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'V':
                count += 1
    return count


def santa_move(matrix, presents):
    santa_pos = find_santa(matrix)
    happy_kids = nice_kids(matrix)
    directions = {
        'up': [-1, 0],
        'right': [0, 1],
        'left': [0, -1],
        'down': [1, 0]
    }
    while presents:
        command = input()

        if command == 'Christmas morning':
            break

        current_move = directions[command][0] + santa_pos[0], directions[command][1] + santa_pos[1]
        if valid_move(current_move[0], current_move[1], matrix):
            if matrix[current_move[0]][current_move[1]] == 'V':
                presents -= 1
            elif matrix[current_move[0]][current_move[1]] == 'C':
                possible_kids = [
                    [current_move[0], current_move[1] + 1],
                    [current_move[0], current_move[1] - 1],
                    [current_move[0] - 1, current_move[1]],
                    [current_move[0] + 1, current_move[1]]
                ]
                for move in possible_kids:
                    if valid_move(move[0], move[1], matrix):
                        if matrix[move[0]][move[1]] in ['V', 'X']:
                            presents -= 1
                            matrix[move[0]][move[1]] = '-'
            matrix[current_move[0]][current_move[1]] = 'S'
            matrix[santa_pos[0]][santa_pos[1]] = '-'
            santa_pos = current_move[0], current_move[1]

    if nice_kids(matrix) == 0:
        output = f'Good job, Santa! {happy_kids} happy nice kid/s.'
    else:
        output = f'No presents for {nice_kids(matrix)} nice kid/s.'

    if not presents and nice_kids(matrix) > 0:
        print('Santa ran out of presents!')

    return '\n'.join([' '.join([str(x) for x in matrix[i]]) for i in range(len(matrix))]) + '\n' + output


presents_count = int(input())
neighbourhood = [[x for x in input().split()] for _ in range(int(input()))]
print(santa_move(neighbourhood, presents_count))
