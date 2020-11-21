movie_budget = float(input())
extras_count = int(input())
price_for_clothes_per_extra = float(input())

stage_price = movie_budget * 0.1
total_price_for_clothes = price_for_clothes_per_extra * extras_count

if extras_count > 150:
    total_price_for_clothes *= 0.9

final_bill = movie_budget - (stage_price + total_price_for_clothes)

if final_bill >= 0:
    print('Action!')
    print(f'Wingard starts filming with {final_bill:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {abs(final_bill):.2f} leva more.')
