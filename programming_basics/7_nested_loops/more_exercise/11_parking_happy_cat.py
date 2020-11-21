def parking_tax(days, hours):
    total_tax = 0

    for day in range(1, days_count + 1):
        daily_tax = 0
        for hour in range(1, hours_count + 1):
            even_day_odd_hour = day % 2 == 0 and hour % 2 == 1
            odd_day_even_hour = day % 2 == 1 and hour % 2 == 0

            if even_day_odd_hour:
                daily_tax += 2.50
            elif odd_day_even_hour:
                daily_tax += 1.25
            else:
                daily_tax += 1

        total_tax += daily_tax
        print(f'Day: {day} - {daily_tax:.2f} leva')

    return f'Total: {total_tax:.2f} leva'


days_count = int(input())
hours_count = int(input())

print(parking_tax(days_count, hours_count))
