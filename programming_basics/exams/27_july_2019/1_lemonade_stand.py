import math

kg_lemons = float(input())
kg_sugar = float(input())
l_water = float(input()) * 1000

ml_lemon_juice = kg_lemons * 980

ml_lemonade = ml_lemon_juice + l_water + (0.3 * kg_sugar)
sold_cups = math.floor(ml_lemonade / 150)
earnings = sold_cups * 1.2

print(f'All cups sold: {sold_cups}')
print(f'Money earned: {earnings:.2f}')
