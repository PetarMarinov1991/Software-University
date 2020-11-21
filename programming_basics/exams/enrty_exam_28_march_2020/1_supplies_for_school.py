pens_count = int(input())
markers_count = int(input())
liters_mr_proper = float(input())
discount = int(input())

price = pens_count * 5.8 + markers_count * 7.2 + liters_mr_proper * 1.2
print(f'{price - ((price * discount) / 100):.3f}')
