days_count = int(input())
hours_count = int(input())

parking_tax = 0
total_tax = 0

for day in range(1, days_count + 1):
    parking_tax = 0
    for hour in range(1, hours_count + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_tax += 2.50
            total_tax += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking_tax += 1.25
            total_tax += 1.25
        else:
            parking_tax += 1
            total_tax += 1

    print(f'Day: {day} - {parking_tax:.2f} leva')
print(f'Total: {total_tax:.2f} leva')
