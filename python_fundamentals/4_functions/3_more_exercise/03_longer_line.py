import math


def find_closest_point(p):
    points = [(p[0], p[1]), (p[6], p[7]), (p[2], p[3]), (p[4], p[5])]
    target = (0, 0)

    result = []

    for i in range(4):
        shortest = min(points, key=lambda point: math.hypot(target[1]-point[1], target[0]-point[0]))
        points.remove(shortest)
        result.append(tuple(int(x) for x in shortest))

    return ''.join([str(x) for x in result][2:])


p = [float(input()) for _ in range(8)]

print(find_closest_point(p))
