string = input().split('#')
water = int(input())

effort = 0
total_fire = 0
valid = False

put_out_cells = []

for command in string:
    arg = command.split(' = ')
    fire_type = arg[0]
    fire_lvl = int(arg[1])

    if water < fire_lvl:
        continue

    if fire_type == 'High' and fire_lvl in range(81, 126):
        valid = True
    elif fire_type == 'Medium' and fire_lvl in range(51, 81):
        valid = True
    elif fire_type == 'Low' and fire_lvl in range(1, 51):
        valid = True

    if valid:
        put_out_cells.append(fire_lvl)
        water -= fire_lvl
        effort += fire_lvl * 0.25
        total_fire += fire_lvl

print('Cells:')

for cell in put_out_cells:
    print(f' - {cell}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
