month = input()
nights = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if nights > 14:
        studio *= 0.7
        apartment *= 0.9
    elif nights > 7:
        studio *= 0.95

elif month == 'June' or month == 'September':
    studio = 75.2
    apartment = 68.7
    if nights > 14:
        studio *= 0.8
        apartment *= 0.9

elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if nights > 14:
        apartment *= 0.9

print(f'Apartment: {nights * apartment:.2f} lv.')
print(f'Studio: {nights * studio:.2f} lv.')
