flowers_kind = input()
flowers_count = int(input())
budget = int(input())

flowers_price = 0

if flowers_kind == 'Roses':
    if flowers_count > 80:
        flowers_price = 5 * flowers_count * 0.9
    else:
        flowers_price = 5 * flowers_count
elif flowers_kind == 'Dahlias':
    if flowers_count > 90:
        flowers_price = 3.8 * flowers_count * 0.85
    else:
        flowers_price = 3.8 * flowers_count
elif flowers_kind == 'Tulips':
    if flowers_count > 80:
        flowers_price = 2.8 * flowers_count * 0.85
    else:
        flowers_price = 2.8 * flowers_count
elif flowers_kind == 'Narcissus':
    if flowers_count < 120:
        flowers_price = 3 * flowers_count * 1.15
    else:
        flowers_price = 3 * flowers_count
elif flowers_kind == 'Gladiolus':
    if flowers_count < 80:
        flowers_price = 2.5 * flowers_count * 1.2
    else:
        flowers_price = 2.5 * flowers_count

diff = budget - flowers_price

if diff >= 0:
    print(f'Hey, you have a great garden with {flowers_count} {flowers_kind} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(diff):.2f} leva more.')
