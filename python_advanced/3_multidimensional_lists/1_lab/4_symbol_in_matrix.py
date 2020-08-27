n = int(input())
matrix = [[x for x in input()] for _ in range(n)]
searched_symbol = input()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_symbol:
            print((row, col))
            exit(0)

print(f'{searched_symbol} does not occur in the matrix')
