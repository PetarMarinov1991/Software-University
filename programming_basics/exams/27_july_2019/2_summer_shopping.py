budget = int(input())
towel_price = float(input())
discount = int(input())

umbrella_price = 2/3 * towel_price
flip_flops_price = 0.75 * umbrella_price
bag_price = 1/3 * (towel_price + flip_flops_price)
total_sum = towel_price + umbrella_price + flip_flops_price + bag_price

total_sum -= total_sum * discount / 100
money_left = abs(budget - total_sum)

if budget >= total_sum:
    print(f'Annie\'s sum is {total_sum:.2f} lv. She has {money_left:.2f} lv. left.')
else:
    print(f'Annie\'s sum is {total_sum:.2f} lv. She needs {money_left:.2f} lv. more.')
