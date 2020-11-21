degrees = int(input())
day_time = input()

outfit = None
shoes = None

if day_time == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif degrees <= 18:
    if day_time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif day_time == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif degrees <= 24:
    if day_time == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
else:
    if day_time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')
