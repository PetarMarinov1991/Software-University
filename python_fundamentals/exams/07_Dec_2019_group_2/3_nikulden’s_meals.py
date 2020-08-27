restaurant = dict()

unlike_meals = 0

while True:
    line = input().split('-')
    command = line[0]

    if command == 'Stop':
        break

    guest, meal = line[1], line[2]
    if command == 'Like':
        if guest not in restaurant:
            restaurant.update({guest: [meal]})
        if meal not in restaurant[guest]:
            restaurant[guest].append(meal)
    elif command == 'Unlike':
        if guest not in restaurant:
            print(f'{guest} is not at the party.')
        elif meal not in restaurant[guest]:
            print(f'{guest} doesn\'t have the {meal} in his/her collection.')
        else:
            print(f'{guest} doesn\'t like the {meal}.')
            restaurant[guest].remove(meal)
            unlike_meals += 1

restaurant = {k: v for k, v in sorted(restaurant.items(), key=lambda x: (-len(x[1]), x[0]))}

for customer, meals in restaurant.items():
    print(f'{customer}: {", ".join([meal for meal in meals])}')
print(f'Unliked meals: {unlike_meals}')
