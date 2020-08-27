capacity = 255
tank = 0

num_of_lines = int(input())

for i in range(num_of_lines):
    water = int(input())

    if water > capacity:
        print('Insufficient capacity!')
    else:
        capacity -= water
        tank += water

print(tank)
