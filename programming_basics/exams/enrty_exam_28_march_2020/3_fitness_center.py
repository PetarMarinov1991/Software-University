from operator import itemgetter

money = float(input())
gender = input()
age = int(input())
sport = input()

cards_prices = {
    'Gym': [42, 35],
    'Boxing': [41, 37],
    'Yoga': [45, 42],
    'Zumba': [34, 31],
    'Dances': [51, 53],
    'Pilates': [39, 37]
}

card_price = 0

if gender == 'm':
    card_price = itemgetter(sport)(cards_prices)[0]
elif gender == 'f':
    card_price = itemgetter(sport)(cards_prices)[1]

if age <= 19:
    card_price *= 0.8

if money >= card_price:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f'You don\'t have enough money! You need ${card_price - money:.2f} more.')
