def get_magic_triangle(num):
    starting_point = [[1], [1, 1]]
    while len(starting_point) < num:
        new_list = [1, 1]
        for i in range(len(starting_point[-1][:-1])):
            new_list.insert(1, starting_point[-1][i] + starting_point[-1][i + 1])
        starting_point.append(new_list)
    return starting_point
