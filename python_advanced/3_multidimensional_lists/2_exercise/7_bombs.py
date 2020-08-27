def is_valid(pos, size):
    return pos[0] in range(size) and pos[1] in range(size)


def explode_cells(r, c, size, my_matrix):
    rows = [-1, -1, -1, 0, 0, 1, 1, 1]
    cols = [-1, 0, 1, -1, 1, -1, 0, 1]
    if my_matrix[r][c] > 0:
        for j in range(8):
            current_pos = [r + rows[j], c + cols[j]]
            if is_valid(current_pos, size):
                if my_matrix[current_pos[0]][current_pos[1]] > 0:
                    my_matrix[current_pos[0]][current_pos[1]] -= my_matrix[r][c]
        my_matrix[r][c] = 0
    return my_matrix


def alive_cells(my_matrix):
    cells = 0
    cells_sum = 0
    for sub_matrix in range(len(my_matrix)):
        for elem in my_matrix[sub_matrix]:
            if elem > 0:
                cells += 1
                cells_sum += elem
    return f'Alive cells: {cells}\n' \
           f'Sum: {cells_sum}'


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = input().split()

for i in range(len(coordinates)):
    row, col = [int(x) for x in coordinates[i].split(',')]
    explode_cells(row, col, n, matrix)

print(alive_cells(matrix))
print('\n'.join([' '.join([str(x) for x in matrix[i]]) for i in range(len(matrix))]))
