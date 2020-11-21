months = int(input())

electricity = 0
water = 0
net = 0
other = 0
other_bill = 0

for i in range(months):
    bill = float(input())

    electricity += bill
    other_bill = (bill + 20 + 15) * 1.2
    other += other_bill

water = 20 * months
net = 15 * months
average = (electricity + water + net + other) / months

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {net:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')
