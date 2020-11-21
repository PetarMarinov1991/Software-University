import math

vineyard_area = int(input())
grapes_per_square_m = float(input())
liters_wine_needed = float(input())
workers_count = int(input())

total_grapes = vineyard_area * grapes_per_square_m
wine_produced = total_grapes * 0.4 / 2.5

diff = wine_produced - liters_wine_needed

if diff >= 0:
    liters_per_person = math.ceil(diff / workers_count)
    print(f'Good harvest this year! Total wine: {math.floor(wine_produced)} liters.')
    print(f'{math.ceil(diff)} liters left -> {liters_per_person} liters per person.')
else:
    print(f'It will be a tough winter! More {abs(math.ceil(diff))} liters wine needed.')

