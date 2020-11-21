target = float(input())
command = input()

income = 0

while command != 'Party!':
    cocktail_name = command
    cocktail_count = int(input())

    cocktail_price = len(cocktail_name) * cocktail_count
    cocktail_last_digit = cocktail_price % 10

    if cocktail_last_digit % 2 != 0:
        cocktail_price *= 0.75
        income += cocktail_price
        target -= cocktail_price
    else:
        income += cocktail_price
        target -= cocktail_price

    if target <= 0:
        print('Target acquired.')
        print(f'Club income - {income:.2f} leva.')
        break

    command = input()

    if command == 'Party!':
        print(f'We need {target:.2f} leva more.')
        print(f'Club income - {income:.2f} leva.')
