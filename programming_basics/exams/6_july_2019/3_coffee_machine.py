drink_type = input()
sugar = input()
drinks_count = int(input())

drink_price = 0
final_price = 0
sugar_discount = False
espresso_discount = False

if sugar == 'Without':

    if drinks_count >= 5:
        espresso_discount = True

    if sugar == 'Extra':
        drink_price = 1.20
    elif sugar == 'Normal':
        drink_price = 1.00
    elif sugar == 'Without':
        drink_price = 0.90
        sugar_discount = True

elif drink_type == 'Cappuccino':
    if sugar == 'Extra':
        drink_price = 1.60
    elif sugar == 'Normal':
        drink_price = 1.20
    elif sugar == 'Without':
        drink_price = 1.00
        sugar_discount = True

elif drink_type == 'Tea':
    if sugar == 'Extra':
        drink_price = 0.70
    elif sugar == 'Normal':
        drink_price = 0.60
    elif sugar == 'Without':
        drink_price = 0.50
        sugar_discount = True

total_price = drink_price * drinks_count
final_price = total_price

if sugar_discount:
    sugar_discount = total_price * 0.35
    final_price = total_price - sugar_discount
if espresso_discount:
    espresso_discount = final_price * 0.25
    final_price -= espresso_discount

if final_price >= 15:
    final_price *= 0.8

print(f'You bought {drinks_count} cups of {drink_type} for {final_price:.2f} lv.')
