budget = float(input())
liters_fuel = float(input())
day_of_week = input()

liters_fuel_price = 2.10
tour_guide_price = 100
total = tour_guide_price + liters_fuel * liters_fuel_price

if day_of_week == 'Saturday':
    total *= 0.9
elif day_of_week == 'Sunday':
    total *= 0.8

diff = abs(budget - total)

if budget >= total:
    print(f'Safari time! Money left: {diff:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')
