cells = input().split('#')
amount_of_water = int(input())

effort = 0
total_fire = 0
cells_down = []

for c in cells:
    cell = c.split(' = ')
    fire_lvl, value = cell[0], int(cell[1])

    high = fire_lvl == 'High' and value in range(81, 126)
    medium = fire_lvl == 'Medium' and value in range(51, 81)
    low = fire_lvl == 'Low' and value in range(1, 51)

    if high or medium or low:
        if amount_of_water >= value:
            amount_of_water -= value
            effort += value * 0.25
            total_fire += value
            cells_down.append(value)

print('Cells:')

for cell in cells_down:
    print(f' - {cell}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
