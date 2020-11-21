cruise_type = input()
cabin_type = input()
nights = int(input())

night_price = 0

if cruise_type == "Mediterranean":
    if cabin_type == "standard cabin":
        night_price = 27.50
    elif cabin_type == "cabin with balcony":
        night_price = 30.20
    elif cabin_type == "apartment":
        night_price = 40.50
elif cruise_type == "Adriatic":
    if cabin_type == "standard cabin":
        night_price = 22.99
    elif cabin_type == "cabin with balcony":
        night_price = 25.00
    elif cabin_type == "apartment":
        night_price = 34.99
elif cruise_type == "Aegean":
    if cabin_type == "standard cabin":
        night_price = 23.00
    elif cabin_type == "cabin with balcony":
        night_price = 26.60
    elif cabin_type == "apartment":
        night_price = 39.80

trip_price = 4 * nights * night_price

if nights > 7:
    trip_price *= 0.75

print(f'Annie\'s holiday in the {cruise_type} sea costs {trip_price:.2f} lv.')
