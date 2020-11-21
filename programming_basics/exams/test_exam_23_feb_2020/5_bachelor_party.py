singer_money = int(input())

reservations_sum = 0
guests = 0

command = input()

while command != 'The restaurant is full':
    group = int(command)
    guests += group

    if group < 5:
        reservations_sum += group * 100
    else:
        reservations_sum += group * 70

    command = input()

if reservations_sum >= singer_money:
    print(f'You have {guests} guests and {reservations_sum - singer_money} leva left.')
else:
    print(f'You have {guests} guests and {reservations_sum} leva income, but no singer.')
