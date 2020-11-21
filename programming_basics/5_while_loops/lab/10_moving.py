width = int(input())
length = int(input())
height = int(input())

space = width * length * height

boxes = input()

while not boxes == 'Done':
    space -= int(boxes)

    if space <= 0:
        print(f'No more free space! You need {abs(space)} Cubic meters more.')
        break

    boxes = input()

if boxes == 'Done':
    print(f'{space} Cubic meters left.')
