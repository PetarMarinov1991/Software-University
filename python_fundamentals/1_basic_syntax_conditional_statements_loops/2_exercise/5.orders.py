n = int(input())
total = 0

for _ in range(n):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    condition_1 = capsule_price < 0.01 or capsule_price > 100
    condition_2 = days < 1 or days > 31
    condition_3 = capsules_per_day < 1 or capsules_per_day > 2000

    if condition_1 or condition_2 or condition_3:
        continue

    order_price = days * capsule_price * capsules_per_day
    total += order_price

    print(f'The price for the coffee is: ${order_price:.2f}')

print(f'Total: ${total:.2f}')
