tank_capacity = 0

n = int(input())

for _ in range(n):
    water = int(input())

    if water + tank_capacity > 255:
        print('Insufficient capacity!')
    else:
        tank_capacity += water

print(tank_capacity)
