season = input()
km_per_month = float(input())

lv_km = 0

if km_per_month <= 5000:
    if season == 'Summer':
        lv_km = 0.9
    elif season == 'Winter':
        lv_km = 1.05
    else:
        lv_km = 0.75
elif km_per_month <= 10000:
    if season == 'Summer':
        lv_km = 1.1
    elif season == 'Winter':
        lv_km = 1.25
    else:
        lv_km = 0.95
else:
    lv_km = 1.45

salary = km_per_month * lv_km * 4 * 0.9
print(f'{salary:.2f}')
