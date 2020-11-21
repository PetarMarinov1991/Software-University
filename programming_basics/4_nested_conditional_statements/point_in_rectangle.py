x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

is_x_inside = False
is_y_inside = False

if x1 <= x <= x2:
    is_x_inside = True
if y1 <= y <= y2:
    is_y_inside = True

if is_x_inside and is_y_inside:
    print('Inside')
else:
    print('Outside')
