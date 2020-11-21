budget = float(input())
season = input()

location = None
accommodation = None
vacation_price = 0

if season == 'Summer':
    location = 'Alaska'
elif season == 'Winter':
    location = 'Morocco'

if budget > 3000:
    accommodation = 'Hotel'
    vacation_price = budget * 0.9
elif budget > 1000:
    accommodation = 'Hut'
    if season == 'Summer':
        vacation_price = budget * 0.8
    elif season == 'Winter':
        vacation_price = budget * 0.6
else:
    accommodation = 'Camp'
    if season == 'Summer':
        vacation_price = budget * 0.65
    elif season == 'Winter':
        vacation_price = budget * 0.45

print(f'{location} - {accommodation} - {vacation_price:.2f}')
