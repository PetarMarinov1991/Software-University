zoo = dict()
areas = dict()

while True:
    info = input()

    if info == 'Last Info':
        break
    else:
        info = info.split(':')
        command, animal, food, area = info[0], info[1], int(info[2]), info[3]

    if command == 'Add':
        if animal not in zoo:
            zoo[animal] = 0
            if area not in areas:
                areas[area] = 0
            areas[area] += 1
        zoo[animal] += food
    elif command == 'Feed':
        if animal in zoo:
            zoo[animal] -= food
            if zoo[animal] <= 0:
                print(f'{animal} was successfully fed')
                del zoo[animal]
                areas[area] -= 1
                if areas[area] <= 0:
                    del areas[area]

animals_sorted = sorted(sorted(zoo.items(), key=lambda a: a[0]), key=lambda b: b[1], reverse=True)
areas_sorted = sorted(areas.items(), key=lambda c: c[1], reverse=True)

print('Animals:')
for animal, food in animals_sorted:
    print(f'{animal} -> {food}g')

print('Areas with hungry animals:')
for area, hungry_animal in areas_sorted:
    print(f'{area} : {hungry_animal}')
