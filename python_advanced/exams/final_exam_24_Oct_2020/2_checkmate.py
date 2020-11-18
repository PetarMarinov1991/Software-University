def find_king(matrix):
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 'K':
                return i, j


def valid_pos(row, col):
    return row in range(8) and col in range(8)


def output(matrix):
    king_pos = find_king(matrix)
    directions = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1], [-1, -1]]
    result = []

    for i in range(8):
        pos_1, pos_2 = king_pos[0] + directions[i][0], king_pos[1] + directions[i][1]
        while valid_pos(pos_1, pos_2):
            if matrix[pos_1][pos_2] == 'Q':
                result.append([pos_1, pos_2])
                break
            pos_1 += directions[i][0]
            pos_2 += directions[i][1]

    if result:
        return '\n'.join([str(x) for x in result])
    return 'The king is safe!'


board = [[x for x in input().split()] for _ in range(8)]
print(output(board))
