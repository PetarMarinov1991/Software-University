exam_hour = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())

exam_in_minutes = (exam_hour * 60) + exam_minutes
arrive_in_minutes = (arrive_hour * 60) + arrive_minutes

late = arrive_in_minutes - exam_in_minutes
early = exam_in_minutes - arrive_in_minutes

if late > 0:
    print(f'Late')
    if late <= 59:
        print(f'{late} minutes after the start')
    else:
        hours = early // 60
        minutes = early % 60
        print(f'{hours}:{minutes:02d} hours after the start')
elif 0 <= early <= 30:
    print(f'On time')
    if early != 0:
        print(f'{early} minutes before the start')
elif early > 30:
    print('Early')
    if early <= 59:
        print(f'{early} minutes before the start')
    else:
        hours = early // 60
        minutes = early % 60
        print(f'{hours}:{minutes:02d} hours before the start')
