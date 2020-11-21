budget = float(input())
season = input()

car = None
car_price = 0

if budget > 500:
    print('Luxury class')
    car = 'Jeep'
    car_price = budget * 0.9
elif budget > 100:
    print('Compact class')
    if season == 'Summer':
        car = 'Cabrio'
        car_price = budget * 0.45
    elif season == 'Winter':
        car = 'Jeep'
        car_price = budget * 0.8
else:
    print('Economy class')
    if season == 'Summer':
        car = 'Cabrio'
        car_price = budget * 0.35
    elif season == 'Winter':
        car = 'Jeep'
        car_price = budget * 0.65

print(f'{car} - {car_price:.2f}')
