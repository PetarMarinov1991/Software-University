def valid_idx(r, c, my_matrix):
    return r in range(len(my_matrix)) and c in range(len(my_matrix[r]))


matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

while True:
    line = input().split()
    command = line[0]

    if command == 'END':
        break

    row, col, num = int(line[1]), int(line[2]), int(line[3])
    if valid_idx(row, col, matrix):
        if command == 'Add':
            matrix[row][col] += num
        elif command == 'Subtract':
            matrix[row][col] -= num
    else:
        print('Invalid coordinates')

print('\n'.join([' '.join([str(x) for x in matrix[i]]) for i in range(len(matrix))]))
