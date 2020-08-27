def closest(x1, y1, x2, y2):
    first_point = abs(x1) + abs(y1)
    second_point = abs(x2) + abs(y2)

    if first_point <= second_point:
        return tuple(sorted([x1, y1]))
    else:
        return tuple(sorted([x2, y2]))


print(closest(x1=int(input()), y1=int(input()), x2=int(input()), y2=int(input())))
