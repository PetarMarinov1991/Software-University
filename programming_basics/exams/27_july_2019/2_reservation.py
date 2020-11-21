booked_day = int(input())
booked_month = int(input())
day_in = int(input())
month_in = int(input())
day_out = int(input())
month_out = int(input())

night_price = 30
discount = 0
diff = day_in - booked_day

if booked_month < month_in:
    night_price = 25
    discount = 0.8
elif diff >= 10:
    night_price = 25

if discount > 0:
    hotel_price = (day_out - day_in) * night_price * discount
else:
    hotel_price = (day_out - day_in) * night_price

print(f'Your stay from {day_in}/{month_in} to {day_out}/{month_out} will cost {hotel_price:.2f}')
