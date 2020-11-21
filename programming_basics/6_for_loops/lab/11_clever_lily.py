age = int(input())
laundry_price = float(input())
toy_price = int(input())

even_birthdays = age // 2
odd_birthdays = even_birthdays
if age % 2 != 0:
    odd_birthdays += 1

savings = odd_birthdays * toy_price + sum([num * 10 for num in range(1, even_birthdays + 1)]) - even_birthdays
diff = abs(savings - laundry_price)

output = 'No!'
if savings >= laundry_price:
    output = 'Yes!'

print(f'{output} {diff:.2f}')
