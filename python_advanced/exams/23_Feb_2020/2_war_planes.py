def plane_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'p':
                return i, j


def total_targets(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 't':
                count += 1
    return count


def directions(direction, move):
    directions_dict = {
        'right': [0, +move],
        'left': [0, -move],
        'up': [-move, 0],
        'down': [+move, 0]
    }
    return directions_dict[direction]


def valid_coordinates(r, c, matrix):
    return r in range(len(matrix)) and c in range(len(matrix[r]))


def mission(matrix):
    plane = plane_pos(matrix)
    all_targets = total_targets(matrix)
    targets_count = total_targets(matrix)
    for _ in range(int(input())):
        line = input().split()
        command, direction, step = line[0], line[1], int(line[2])
        move_1 = plane[0] + directions(direction, step)[0]
        move_2 = plane[1] + directions(direction, step)[1]
        if valid_coordinates(move_1, move_2, matrix):
            if command == 'move':
                if matrix[move_1][move_2] == '.':
                    matrix[plane[0]][plane[1]] = '.'
                    matrix[move_1][move_2] = 'p'
                    plane = move_1, move_2
            elif command == 'shoot':
                if matrix[move_1][move_2] == 't':
                    matrix[move_1][move_2] = 'x'
                    targets_count -= 1
                    if targets_count == 0:
                        return f'Mission accomplished! All {all_targets} targets destroyed.'
                matrix[move_1][move_2] = 'x'
    if targets_count > 0:
        return f'Mission failed! {targets_count} targets left.'


def output(matrix):
    return mission(matrix) + '\n' + '\n'.join([' '.join([str(x) for x in matrix[i]]) for i in range(len(matrix))])


field = [input().split() for _ in range(int(input()))]
print(output(field))

