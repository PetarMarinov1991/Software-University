days = int(input())
food = float(input())

biscuits = 0
dog_eaten = 0
cat_eaten = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())

    dog_eaten += dog_food
    cat_eaten += cat_food

    if day % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1

total_eaten = dog_eaten + cat_eaten

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{total_eaten / food * 100:.2f}% of the food has been eaten.')
print(f'{dog_eaten / total_eaten * 100:.2f}% eaten from the dog.')
print(f'{cat_eaten / total_eaten * 100:.2f}% eaten from the cat.')
