coffees = 0

while True:
    command = input()

    if command == 'END':
        break

    valid_commands = ['coding', 'dog', 'cat', 'movie']

    if command in valid_commands:
        coffees += 1
    elif command.lower() in valid_commands:
        coffees += 2

print('You need extra sleep') if coffees > 5 else print(coffees)
