from math import ceil

sushi = input()
restaurant = input()
portions = int(input())
order = input()

price = 0

if restaurant == 'Sushi Zone':
    if sushi == 'sashimi':
        price = 4.99
    elif sushi == 'maki':
        price = 5.29
    elif sushi == 'uramaki':
        price = 5.99
    elif sushi == 'temaki':
        price = 4.29
elif restaurant == 'Sushi Time':
    if sushi == 'sashimi':
        price = 5.49
    elif sushi == 'maki':
        price = 4.69
    elif sushi == 'uramaki':
        price = 4.49
    elif sushi == 'temaki':
        price = 5.19
elif restaurant == 'Sushi Bar':
    if sushi == 'sashimi':
        price = 5.25
    elif sushi == 'maki':
        price = 5.55
    elif sushi == 'uramaki':
        price = 6.25
    elif sushi == 'temaki':
        price = 4.75
elif restaurant == 'Asian Pub':
    if sushi == 'sashimi':
        price = 4.50
    elif sushi == 'maki':
        price = 4.80
    elif sushi == 'uramaki':
        price = 5.50
    elif sushi == 'temaki':
        price = 5.50
else:
    print(f'{restaurant} is invalid restaurant!')
    exit(0)

total_price = price * portions

if order == 'Y':
    total_price *= 1.2

print(f'Total price: {ceil(total_price)} lv.')
