health = int(input())

frags = 0

while True:
    command = input()

    if command == 'End of battle':
        print(f'Won battles: {frags}. Energy left: {health}')
        break

    if int(command) <= health:
        health -= int(command)
        frags += 1
        if frags % 3 == 0:
            health += frags
    else:
        print(f'Not enough energy! Game ends with {frags} won battles and {health} energy')
        break
