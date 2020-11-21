food = int(input()) * 1000

while True:
    command = input()

    if command == 'Adopted':
        break

    food -= int(command)

if food >= 0:
    print(f'Food is enough! Leftovers: {food} grams.')
else:
    print(f'Food is not enough. You need {abs(food)} grams more.')
