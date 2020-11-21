plane_capacity = float(input())

suitcases_count = 0

while True:
    suitcase = input()

    if suitcase == 'End':
        print('Congratulations! All suitcases are loaded!')
        break

    suitcases_count += 1

    if suitcases_count % 3 == 0:
        plane_capacity -= float(suitcase) * 1.1
    else:
        plane_capacity -= float(suitcase)

    if plane_capacity <= 0:
        print('No more space!')
        suitcases_count -= 1
        break

print(f'Statistic: {suitcases_count} suitcases loaded.')
