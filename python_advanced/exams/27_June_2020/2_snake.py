def find_snake(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'S':
                return i, j


def find_liars(matrix):
    liars = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'B':
                liars.append([i, j])
    return liars


def snake_move(matrix, directions, my_move):
    snake_pos = find_snake(matrix)
    return [directions[my_move][0] + snake_pos[0], directions[my_move][1] + snake_pos[1]]


def valid_move(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix))


paths = {
    'up': [-1, 0],
    'left': [0, -1],
    'right': [0, 1],
    'down': [1, 0]
}
field = [[x for x in input()] for _ in range(int(input()))]
food_quantity = 0

while food_quantity < 10:
    move = input()
    previous_pos = find_snake(field)
    snake = snake_move(field, paths, move)
    if valid_move(snake[0], snake[1], field):
        if field[snake[0]][snake[1]] == '*':
            food_quantity += 1
            field[snake[0]][snake[1]] = 'S'
        elif field[snake[0]][snake[1]] == 'B':
            first_liar, second_liar = find_liars(field)[0], find_liars(field)[1]
            if snake == first_liar:
                field[first_liar[0]][first_liar[1]] = '.'
                field[second_liar[0]][second_liar[1]] = 'S'
                snake = second_liar
            elif snake == second_liar:
                field[second_liar[0]][second_liar[1]] = '.'
                field[first_liar[0]][first_liar[1]] = 'S'
                snake = first_liar
        elif field[snake[0]][snake[1]] == '-':
            field[snake[0]][snake[1]] = 'S'
        field[previous_pos[0]][previous_pos[1]] = '.'
    else:
        field[previous_pos[0]][previous_pos[1]] = '.'
        break

if food_quantity == 10:
    print('You won! You fed the snake.')
else:
    print('Game over!')

print(f'Food eaten: {food_quantity}')
print('\n'.join([''.join([str(x) for x in field[i]]) for i in range(len(field))]))
