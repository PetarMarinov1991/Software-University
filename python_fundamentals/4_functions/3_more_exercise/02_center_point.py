import math


def find_closest_point(x1, y1, x2, y2):
    points = [(x1, y1), (x2, y2)]
    target = (0, 0)
    closest = min(points, key=lambda point: math.hypot(target[1]-point[1], target[0]-point[0]))

    return f'{tuple(int(x) for x in closest)}'


p = [float(input()) for _ in range(4)]
print(find_closest_point(p[0], p[1], p[2], p[3]))
