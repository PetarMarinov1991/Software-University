def get_best_sub_matrix(my_matrix):
    best_sum = 0
    best_sub_matrix = []
    for row in range(len(my_matrix) - 1):
        for col in range(len(my_matrix[row]) - 1):
            a = my_matrix[row][col]
            b = my_matrix[row][col + 1]
            c = my_matrix[row + 1][col]
            d = my_matrix[row + 1][col + 1]
            current_sum = a + b + c + d
            if current_sum > best_sum:
                best_sum = current_sum
                best_sub_matrix = [a, b], [c, d]

    return f'{" ".join([str(x) for x in best_sub_matrix[0]])}\n' \
           f'{" ".join([str(x) for x in best_sub_matrix[1]])}\n' \
           f'{best_sum}'


matrix = [[int(x) for x in input().split(', ')] for _ in range([int(x) for x in input().split(', ')][0])]
print(get_best_sub_matrix(matrix))
