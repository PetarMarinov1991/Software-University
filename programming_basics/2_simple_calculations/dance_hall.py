import math

l = float(input())
w = float(input())
a = float(input())

hall_area = (l * 100) * (w * 100)
wardrobe_area = (a * 100) * (a * 100)
bench_area = hall_area / 10
free_area = hall_area - wardrobe_area - bench_area
dancers_count = free_area / (40 + 7000)

print(math.floor(dancers_count))
