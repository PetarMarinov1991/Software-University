fire_levels = input().split('#')
water = int(input())

cells = []
effort = 0

for data in fire_levels:
    data = data.split(' = ')
    fire = data[0]
    value = int(data[1])

    valid = False

    condition_1 = fire == 'High' and value in range(81, 126)
    condition_2 = fire == 'Medium' and value in range(51, 81)
    condition_3 = fire == 'Low' and value in range(1, 51)

    if condition_1 or condition_2 or condition_3:
        valid = True

    if valid and water - value >= 0:
        effort += value * 0.25
        water -= value
        cells.append(value)

print('Cells:')
for cell in cells:
    print(f'- {cell}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(cells)}')
