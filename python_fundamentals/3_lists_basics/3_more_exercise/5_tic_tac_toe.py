def possibilities(matrix):
    first_diagonal = [matrix[i][i] for i in range(len(matrix))]
    second_diagonal = [(matrix[::-1])[i][i] for i in range(len(matrix))]
    rows = [matrix[i] for i in range(len(matrix))]
    cols = [[row[i] for row in matrix] for i in range(len(matrix))]
    return [first_diagonal] + [second_diagonal] + rows + cols


def determine_winner(matrix):
    for row in possibilities(matrix):
        if len(set(row)) == 1:
            if row[0] == 1:
                return 'First player won'
            elif row[0] == 2:
                return 'Second player won'
    return 'Draw!'


game_board = list([int(x) for x in input().split()] for _ in range(3))

print(determine_winner(game_board))
