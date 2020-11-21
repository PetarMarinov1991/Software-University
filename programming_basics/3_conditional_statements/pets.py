import math

days = int(input())
kg_food_left = int(input())
kg_dog_food = float(input())
kg_cat_food = float(input())
gr_turtle_food = float(input())

dog_food_needed = days * kg_dog_food
cat_food_needed = days * kg_cat_food
turtle_food_needed = days * gr_turtle_food / 1000
total_food_needed = dog_food_needed + cat_food_needed + turtle_food_needed

diff = kg_food_left - total_food_needed
if diff >= 0:
    print(f'{math.floor(diff)} kilos of food left.')
else:
    print(f'{abs(math.floor(diff))} more kilos of food are needed.')

