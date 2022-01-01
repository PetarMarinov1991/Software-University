data = input().split('#')
water = int(input())

effort = 0
cells = []

for fire_info in data:
    args = fire_info.split(' = ')
    fire_type, fire_lvl = args[0], int(args[1])

    valid_cell = True \
        if fire_type == 'High' and fire_lvl in range(81, 126) \
        or fire_type == 'Medium' and fire_lvl in range(51, 81) \
        or fire_type == 'Low' and fire_lvl in range(1, 51) \
        else False

    if valid_cell:
        if water >= fire_lvl:
            water -= fire_lvl
            effort += fire_lvl * 0.25
            cells.append(fire_lvl)

print(f'Cells:\n' + "\n".join(['- ' + str(cell) for cell in cells]))
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(cells)}')
