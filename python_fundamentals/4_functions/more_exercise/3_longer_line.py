from math import sqrt


def closest(x1, y1, x2, y2):
    first = sqrt((abs(x1)) ** 2 + sqrt(abs(y1)) ** 2)
    second = sqrt((abs(x2)) ** 2 + sqrt(abs(y2)) ** 2)

    if first > second:
        return f'({x2}, {y2})({x1}, {y1})'
    else:
        return f'({x1}, {y1})({x2}, {y2})'


def longest_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_line = sqrt(abs(x1 - x2) ** 2) + abs(y1 - y2) ** 2
    second_line = sqrt(abs(x3 - x4) ** 2) + abs(y3 - y4) ** 2

    if first_line >= second_line:
        return closest(x1, y1, x2, y2)
    else:
        return closest(x3, y3, x4, y4)


print(longest_line(
    x1=int(input()), y1=int(input()), x2=int(input()), y2=int(input()),
    x3=int(input()), y3=int(input()), x4=int(input()), y4=int(input())))
