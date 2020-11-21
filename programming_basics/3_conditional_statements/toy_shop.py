holiday_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

profit = puzzles_count * 2.6 + dolls_count * 3 + teddy_bears_count * 4.1 + minions_count * 8.2 + trucks_count * 2
toys_count = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count

discount = 0
if toys_count >= 50:
    discount = profit * 0.25

final_price = profit - discount
rent = final_price * 0.1
total_profit = final_price - rent

diff = abs(total_profit - holiday_price)
if total_profit >= holiday_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
