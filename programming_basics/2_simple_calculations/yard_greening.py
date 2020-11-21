yard_area = float(input())
price_per_yard = 7.61
greening_price = yard_area * price_per_yard
discount = 0.18 * greening_price
total_price = greening_price - discount

print(f'The final price is: {total_price:.2f} lv.\nThe discount is: {discount:.2f} lv.')
