budget = float(input())
video_card_quantity = int(input())
cpu_quantity = int(input())
ram_quantity = int(input())

video_card_price = video_card_quantity * 250
cpu_price = cpu_quantity * (video_card_price * 0.35)
ram_price = ram_quantity * (video_card_price * 0.10)
total_price = video_card_price + cpu_price + ram_price

if video_card_quantity > cpu_quantity:
    total_price *= 0.85

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
