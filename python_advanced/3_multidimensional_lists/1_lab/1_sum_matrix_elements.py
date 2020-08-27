matrix = [[int(x) for x in input().split(', ')] for _ in range([int(x) for x in input().split(', ')][0])]
matrix_sum = sum([sum(sub_matrix) for sub_matrix in matrix])

print(matrix_sum)
print(matrix)
