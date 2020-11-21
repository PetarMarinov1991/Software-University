floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    if floor < floors:
        print()
    for apartment in range(rooms):
        if floor == floors:
            print(f'L{floor}{apartment}', end=' ')
        elif floor % 2 == 0:
            print(f'O{floor}{apartment}', end=' ')
        else:
            print(f'A{floor}{apartment}', end=' ')
