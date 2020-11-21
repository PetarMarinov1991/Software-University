budget = int(input())
season = input()
fisherman_count = int(input())

rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Winter':
    rent = 2600
else:
    rent = 4200

if fisherman_count >= 12:
    rent *= 0.75
elif fisherman_count <= 6:
    rent *= 0.9
else:
    rent *= 0.85

if fisherman_count % 2 == 0 and season != 'Autumn':
    rent *= 0.95

diff = budget - rent

if diff >= 0:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(diff):.2f} leva.')
