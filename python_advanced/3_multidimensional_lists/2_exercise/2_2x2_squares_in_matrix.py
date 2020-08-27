def get_equal_sub_matrix_count(my_matrix):
    count = 0
    for row in range(len(my_matrix) - 1):
        for col in range(len(my_matrix[row]) - 1):
            a = my_matrix[row][col]
            b = my_matrix[row][col + 1]
            c = my_matrix[row + 1][col]
            d = my_matrix[row + 1][col + 1]
            if a == b == c == d:
                count += 1
    return count


matrix = [[x for x in input().split()] for _ in range([int(x) for x in input().split()][0])]
print(get_equal_sub_matrix_count(matrix))
