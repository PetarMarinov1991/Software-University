def find_max(my_list):
    max_intersection = max(my_list, key=len)
    max_length = max(map(len, my_list))
    return f'Longest intersection is {max_intersection} with length {max_length}'


def define_groups(idx, collection):
    my_range = collection[idx].split(',')
    my_group = set([num for num in range(int(my_range[0]), int(my_range[1]) + 1)])
    return my_group


intersections = []

for _ in range(int(input())):
    ranges = input().split('-')
    first_group, second_group = [], []

    for i in range(len(ranges)):
        first_group = define_groups(i, ranges)
        second_group = define_groups(i + 1, ranges)
        break

    intersections.append(list(first_group.intersection(second_group)))

print(find_max(intersections))
