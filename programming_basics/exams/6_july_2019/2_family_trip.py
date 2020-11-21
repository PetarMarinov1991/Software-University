budget = float(input())
nights_count = int(input())
night_price = float(input())
extra_expenses_percentage = int(input())

if nights_count > 7:
    night_price *= 0.95

all_nights_price = night_price * nights_count
extra_expenses = budget * (extra_expenses_percentage * 1 / 100)
total_money = all_nights_price + extra_expenses

diff = abs(budget - total_money)

if budget >= total_money:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')
