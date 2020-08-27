cars = dict()

for _ in range(int(input())):
    info = input().split('|')
    car, mileage, fuel = info
    cars.update({car: [int(mileage), int(fuel)]})

while True:
    line = input().split(' : ')
    command = line[0]

    if command == 'Stop':
        break

    car = line[1]
    if command == 'Drive':
        distance, fuel = int(line[2]), int(line[3])
        if fuel > cars[car][1]:
            print('Not enough fuel to make that ride')
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            if cars[car][0] >= 100000:
                del cars[car]
                print(f'Time to sell the {car}!')

    elif command == 'Refuel':
        fuel = int(line[2])
        cars[car][1] += fuel
        if cars[car][1] > 75:
            print(f'{car} refueled with {75 - (cars[car][1] - fuel)} liters')
            cars[car][1] = 75
        else:
            print(f'{car} refueled with {fuel} liters')

    elif command == 'Revert':
        kilometers = int(line[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')

cars = {k: v for k, v in sorted(cars.items(), key=lambda x: (-x[1][0], x[0]))}

for car, value in cars.items():
    print(f'{car} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')
