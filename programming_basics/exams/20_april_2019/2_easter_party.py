guests = int(input())
couvert = float(input())
budget = float(input())

cake_price = budget * 0.1
couvert_price = guests * couvert

if guests > 20:
    couvert_price *= 0.75
elif 15 < guests <= 20:
    couvert_price *= 0.80
elif 10 <= guests <= 15:
    couvert_price *= 0.85

total_sum = couvert_price + cake_price
diff = budget - total_sum

if total_sum <= budget:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {abs(diff):.2f} leva needed.')
