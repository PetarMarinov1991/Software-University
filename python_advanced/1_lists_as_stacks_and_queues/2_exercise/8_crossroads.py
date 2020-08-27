from collections import deque

green_light = int(input())
yellow_light = int(input())

green_seconds = green_light
yellow_seconds = yellow_light
passed_cars = 0

while True:
    command = input()

    if command == 'END':
        break

    if command == 'green':
        green_seconds = green_light
        yellow_seconds = yellow_light
        continue

    car_name = command
    car = deque(command)

    while green_seconds:
        if car:
            car.popleft()
            green_seconds -= 1
        else:
            passed_cars += 1
            break
    if car and ''.join(car) != car_name:
        while yellow_seconds:
            if car:
                car.popleft()
                yellow_seconds -= 1
            else:
                passed_cars += 1
                break
        if car:
            print('A crash happened!')
            print(f'{car_name} was hit at {car.popleft()}.')
            exit(0)

print('Everyone is safe.')
print(f'{passed_cars} total cars passed the crossroads.')
