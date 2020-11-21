season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

price_per_student = 0
sport = None

if season == 'Summer':
    price_per_student = 15
    if group_type == 'boys':
        sport = 'Football'
    elif group_type == 'girls':
        sport = 'Volleyball'
    else:
        price_per_student = 20
        sport = 'Swimming'
elif season == 'Spring':
    price_per_student = 7.2
    if group_type == 'boys':
        sport = 'Tennis'
    elif group_type == 'girls':
        sport = 'Athletics'
    else:
        price_per_student = 9.5
        sport = 'Cycling'
else:
    price_per_student = 9.6
    if group_type == 'boys':
        sport = 'Judo'
    elif group_type == 'girls':
        sport = 'Gymnastics'
    else:
        price_per_student = 10
        sport = 'Ski'

vacation_price = price_per_student * students_count * nights_count

if students_count >= 50:
    vacation_price -= vacation_price * 0.5
elif students_count >= 20:
    vacation_price -= vacation_price * 0.15
elif students_count >= 10:
    vacation_price -= vacation_price * 0.05

print(f'{sport} {vacation_price:.2f} lv.')
