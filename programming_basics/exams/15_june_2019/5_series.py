budget = float(input())
series_count = int(input())

total = 0

for series in range(series_count):
    series_title = input()
    series_price = float(input())

    if series_title == 'Thrones':
        series_price *= 0.50
    elif series_title == 'Lucifer':
        series_price *= 0.60
    elif series_title == 'Protector':
        series_price *= 0.70
    elif series_title == 'TotalDrama':
        series_price *= 0.80
    elif series_title == 'Area':
        series_price *= 0.90

    total += series_price

diff = abs(budget - total)

if budget >= total:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {diff:.2f} lv. more to buy the series!')
