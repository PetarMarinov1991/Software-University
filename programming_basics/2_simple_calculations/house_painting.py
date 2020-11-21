x = float(input())
y = float(input())
h = float(input())

entrance = 2.4
window = 2.25
side = x * y
two_sides = 2 * side - 2 * window
back_side = x ** 2
front_and_back = 2 * back_side - entrance
walls_area = two_sides + front_and_back

roof_rectangles = 2 * side
roof_triangles = 2 * (x * h / 2)
roof_area = roof_rectangles + roof_triangles

green_paint = walls_area / 3.4
red_paint = roof_area / 4.3

print(f'{green_paint:.2f}\n{red_paint:.2f}')

