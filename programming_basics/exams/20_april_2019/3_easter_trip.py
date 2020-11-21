destination = input()
booking = input()
nights = int(input())

night_price = 0

if destination == 'France':
    if booking == '21-23':
        night_price = 30
    elif booking == '24-27':
        night_price = 35
    elif booking == '28-31':
        night_price = 40

elif destination == 'Italy':
    if booking == '21-23':
        night_price = 28
    elif booking == '24-27':
        night_price = 32
    elif booking == '28-31':
        night_price = 39

elif destination == 'Germany':
    if booking == '21-23':
        night_price = 32
    elif booking == '24-27':
        night_price = 37
    elif booking == '28-31':
        night_price = 43

trip_cost = night_price * nights

print(f'Easter trip to {destination} : {trip_cost:.2f} leva.')
