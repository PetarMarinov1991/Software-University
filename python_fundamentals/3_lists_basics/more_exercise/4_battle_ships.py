lines = int(input())

matrix_str = [input().split() for row in range(lines)]
matrix = [list(map(int, row)) for row in matrix_str]

attacks = input().split()

destroyed_ships = 0

for idx in attacks:
    row = int(idx[0])
    col = int(idx[2])

    if matrix[row][col] > 0:
        matrix[row][col] -= 1
        if matrix[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)
