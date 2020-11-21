year_tax = int(input())

sneakers_price = year_tax * 0.6
suit_price = sneakers_price * 0.8
ball_price = suit_price * 0.25
accessories_price = ball_price * 0.2

total_price = year_tax + sneakers_price + suit_price + ball_price + accessories_price

print(f'{total_price:.2f}')
