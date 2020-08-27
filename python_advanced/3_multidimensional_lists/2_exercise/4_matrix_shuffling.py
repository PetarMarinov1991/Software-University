def valid_input(data, my_matrix):
    if data[0] == 'swap':
        if len(data) == 5:
            a, b, c, d = int(data[1]), int(data[2]), int(data[3]), int(data[4])
            if a in range(len(my_matrix)) and b in range(len(my_matrix[a])):
                if c in range(len(my_matrix)) and d in range(len(my_matrix[c])):
                    return True
    return False


def swap_elements(a, b, c, d, my_matrix):
    my_matrix[a][b], my_matrix[c][d] = my_matrix[c][d], my_matrix[a][b]
    return '\n'.join([' '.join([str(x) for x in my_matrix[i]]) for i in range(len(my_matrix))])


matrix = [[x for x in input().split()] for _ in range([int(x) for x in input().split()][0])]

while True:
    line = input().split()

    if line[0] == 'END':
        break

    if valid_input(line, matrix):
        elements = [int(x) for x in line[1:]]
        print(swap_elements(elements[0], elements[1], elements[2], elements[3], matrix))
    else:
        print('Invalid input!')
