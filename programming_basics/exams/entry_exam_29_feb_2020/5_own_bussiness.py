width = int(input())
length = int(input())
height = int(input())

space = width * length * height

command = input()

while not command == 'Done':
    computers = command
    space -= int(computers)

    if space <= 0:
        print(f'No more free space! You need {abs(space)} Cubic meters more.')
        break

    command = input()

print(f'{space} Cubic meters left.')
