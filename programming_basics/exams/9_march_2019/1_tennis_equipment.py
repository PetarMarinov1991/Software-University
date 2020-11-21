import math

tennis_racket_price = float(input())
tennis_rackets_count = int(input())
sneakers_pears_count = int(input())

total_tennis_rackets = tennis_racket_price * tennis_rackets_count
sneakers_pears_price = (tennis_racket_price / 6) * sneakers_pears_count
equipment_price = (total_tennis_rackets + sneakers_pears_price) * 0.2

total_price = total_tennis_rackets + sneakers_pears_price + equipment_price

djokovic_bill = total_price / 8
sponsors_bill = total_price - djokovic_bill

print(f'Price to be paid by Djokovic {math.floor(djokovic_bill)}')
print(f'Price to be paid by sponsors {math.ceil(sponsors_bill)}')
