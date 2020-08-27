row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
col_1 = [row_1[0], row_2[0], row_3[0]]
col_2 = [row_1[1], row_2[1], row_3[1]]
col_3 = [row_1[2], row_2[2], row_3[2]]
diagonal_1 = [row_1[0], row_2[1], row_3[2]]
diagonal_2 = [row_1[2], row_2[1], row_3[0]]

possibilities = [row_1, row_2, row_3, col_1, col_2, col_3, diagonal_1, diagonal_2]

for line in possibilities:
    if line.count('1') == 3:
        print('First player won')
        exit(0)
    elif line.count('2') == 3:
        print('Second player won')
        exit(0)

print('Draw!')
