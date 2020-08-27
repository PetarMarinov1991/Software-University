chairs = []
taken_places = []

free_chairs = 0

for num in range(1, int(input()) + 1):
    room = input().split()
    chairs, taken_places = len(room[0]), int(room[1])

    diff = taken_places - chairs

    if taken_places > chairs:
        print(f'{diff} more chairs needed in room {num}')
        free_chairs -= diff
    else:
        free_chairs += abs(diff)

if free_chairs >= 0:
    print(f'Game On, {free_chairs} free chairs left')
