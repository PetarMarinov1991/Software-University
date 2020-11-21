tables_count = int(input())
tables_length = float(input())
tables_width = float(input())

covers_area = tables_count * (tables_length + 0.6) * (tables_width + 0.6)
squares_area = tables_count * (tables_length / 2) * (tables_length / 2)

usd_price = covers_area * 7 + squares_area * 9
bgn_price = usd_price * 1.85

print(f'{usd_price:.2f} USD\n{bgn_price:.2f} BGN')
