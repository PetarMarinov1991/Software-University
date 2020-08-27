parking = []

for _ in range(int(input())):
    line = input().split(', ')
    direction, car_number = line[0], line[1]

    if direction == 'IN':
        if car_number not in parking:
            parking.append(car_number)
    elif direction == 'OUT':
        if car_number in parking:
            parking.remove(car_number)

if parking:
    print('\n'.join([car for car in parking]))
else:
    print('Parking Lot is Empty')
