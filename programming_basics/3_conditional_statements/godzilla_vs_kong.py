budget = float(input())
statistics = int(input())
clothes = float(input())

decor = budget * 0.1
clothes_price = clothes * statistics

if statistics >= 150:
    clothes_price *= 0.9

total_costs = decor + clothes_price
money_left = budget - total_costs

if money_left >= 0:
    print(f'Action!\nWingard starts filming with {money_left:.2f} leva left.')
else:
    print(f'Not enough money!\nWingard needs {abs(money_left):.2f} leva more.')
