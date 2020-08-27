matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
diagonal_sum = sum([matrix[i][i] for i in range(len(matrix))])

print(diagonal_sum)
