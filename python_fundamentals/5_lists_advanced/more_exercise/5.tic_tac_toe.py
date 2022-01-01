def unpack(input_data):
    return [int(x) for x in input_data.split()]


def get_col(arr, col):
    return list(map(lambda x: x[col], arr))


def play_board_data(matrix):
    first_diagonal = [matrix[i][i] for i in range(len(matrix))]
    second_diagonal = [matrix[len(matrix) - 1 - i][i] for i in range(len(matrix))]
    cols = [get_col(matrix, i) for i in range(len(matrix))]
    rows = matrix

    play_board = [first_diagonal, second_diagonal]

    for c in cols:
        play_board.append(c)
    for r in rows:
        play_board.append(r)

    return play_board


def checkList(lst):
    return len(set(lst)) == 1


def winner(matrix):
    matrix = play_board_data(matrix)
    for i in range(len(matrix)):
        if checkList(matrix[i]):
            if matrix[i][0] == 1:
                return 'First player won'
            elif matrix[i][0] == 2:
                return 'Second player won'
    return 'Draw!'


tic_tac_toe = [unpack(input()), unpack(input()), unpack(input())]

print(winner(tic_tac_toe))
