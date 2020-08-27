def valid_move(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix[row]))


def find_bunny(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'B':
                return i, j


def directions(matrix):
    paths = {
        0: ['up', 0, []],
        1: ['left', 0, []],
        2: ['right', 0, []],
        3: ['down', 0, []]
    }
    bunny_pos = find_bunny(matrix)
    moves = [
        [bunny_pos[0] - 1, bunny_pos[1]],
        [bunny_pos[0], bunny_pos[1] - 1],
        [bunny_pos[0], bunny_pos[1] + 1],
        [bunny_pos[0] + 1, bunny_pos[1]]
    ]
    for i in range(4):
        while valid_move(moves[i][0], moves[i][1], matrix) and matrix[moves[i][0]][moves[i][1]] != 'X':
            paths[i][1] += matrix[moves[i][0]][moves[i][1]]
            paths[i][2].append([moves[i][0], moves[i][1]])
            if i == 0 or i == 1:
                moves[i][i] -= 1
            elif i == 2:
                moves[i][1] += 1
            elif i == 3:
                moves[i][0] += 1
    return paths


field = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(int(input()))]
for _, value in sorted(directions(field).items(), key=lambda x: -x[1][1]):
    print(value[0])
    print('\n'.join([str(x) for x in value[2]]))
    print(value[1])
    break
