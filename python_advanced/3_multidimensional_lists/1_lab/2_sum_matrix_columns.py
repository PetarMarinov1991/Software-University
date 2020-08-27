matrix = [[int(x) for x in input().split()] for _ in range([int(x) for x in input().split(', ')][0])]
cols_sum = [sum([row[i] for row in matrix]) for i in range(len(matrix[0]))]

print('\n'.join([str(x) for x in cols_sum]))
