from collections import deque


def concatenate(str_1, str_2, arr):
    valid_color = ''
    if str_1 + str_2 in arr:
        valid_color = str_1 + str_2
    elif str_2 + str_1 in arr:
        valid_color = str_2 + str_1
    return valid_color


def cut_char(str_1, str_2):
    new_str_1, new_str_2 = '', ''
    if len(str_1) > 0:
        new_str_1 = str_1[:-1]
    if len(str_2) > 0:
        new_str_2 = str_2[:-1]
    return new_str_1, new_str_2


def filter_colors(colors):
    if 'orange' in colors and not all(x in colors for x in ['yellow', 'red']):
        colors.remove('orange')
    if 'purple' in colors and not all(x in colors for x in ['blue', 'red']):
        colors.remove('purple')
    if 'green' in colors and not all(x in colors for x in ['yellow', 'blue']):
        colors.remove('blue')
    return colors


string = input().split()

all_colors = ['yellow', 'blue', 'red', 'orange', 'purple', 'green']
collection = deque(string)
result = []

while collection:
    first_elem, second_elem = collection.popleft(), ''
    if collection:
        second_elem = collection.pop()

    color = concatenate(first_elem, second_elem, all_colors)

    if color:
        result.append(color)
    else:
        first_return, second_return = cut_char(first_elem, second_elem)
        idx_to_return = len(collection) // 2
        if first_return:
            collection.insert(idx_to_return, first_return)
        if second_return:
            collection.insert(idx_to_return, second_return)

print(filter_colors(result))
