import sys


def get_max_sub_matrix_sum(my_matrix):
    best_sum = -sys.maxsize - 1
    best_matrix = []
    for row in range(len(my_matrix) - 2):
        for col in range(len(my_matrix[row]) - 2):
            current_matrix = [[my_matrix[i][j] for j in range(col, col + 3)] for i in range(row, row + 3)]
            current_sum = sum([sum(x) for x in current_matrix])
            if current_sum > best_sum:
                best_sum = current_sum
                best_matrix = current_matrix

    return f'Sum = {best_sum}\n' + \
           "\n".join([x for x in [" ".join([str(x) for x in best_matrix[i]]) for i in range(len(best_matrix))]])


matrix = [[int(x) for x in input().split()] for _ in range([int(x) for x in input().split()][0])]
print(get_max_sub_matrix_sum(matrix))
