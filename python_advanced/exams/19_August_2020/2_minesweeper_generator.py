def valid_coordinates(r, c, matrix):
    return r in range(len(matrix)) and c in range(len(matrix[r]))


def directions():
    rows = [-1, -1, -1, 0, 0, 1, 1, 1]
    cols = [-1, 0, 1, -1, 1, -1, 0, 1]
    cells = [[rows[i], cols[i]] for i in range(8)]
    return cells


def fill_cells(matrix):
    for i in coordinates:
        row, col = i[0], i[1]
        if valid_coordinates(row, col, matrix):
            matrix[row][col] = '*'
            for x in directions():
                check_row, check_col = x[0] + row, x[1] + col
                if valid_coordinates(check_row, check_col, matrix) and matrix[check_row][check_col] != '*':
                    matrix[check_row][check_col] += 1
    return '\n'.join([' '.join([str(x) for x in matrix[i]]) for i in range(len(matrix))])


size = int(input())
field = [[0 for x in range(size)] for _ in range(size)]
coordinates = [[int(x) for x in input().strip('()').split(', ')] for _ in range(int(input()))]

print(fill_cells(field))
