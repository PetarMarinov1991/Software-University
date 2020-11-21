distance = int(input())
day_or_night = input()

trip_price = 0

if distance >= 100:
    trip_price = distance * 0.06
elif distance >= 20:
    trip_price = distance * 0.09
else:
    if day_or_night == 'day':
        trip_price = 0.70 + distance * 0.79
    elif day_or_night == 'night':
        trip_price = 0.70 + distance * 0.90

print(f'{trip_price:.2f}')
