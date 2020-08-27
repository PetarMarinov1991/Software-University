matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
first_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
print("First diagonal: " + ', '.join([str(x) for x in first_diagonal]) + f". Sum: {sum(first_diagonal)}")
print("Second diagonal: " + ', '.join([str(x) for x in second_diagonal]) + f". Sum: {sum(second_diagonal)}")
