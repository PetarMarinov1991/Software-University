command = input()
sorting_students = True

while command != 'Welcome!':
    name = command
    house = ''

    if name == 'Voldemort':
        sorting_students = False
        print('You must not speak of that name!')
        break

    if len(name) < 5:
        house = 'Gryffindor'
    elif len(name) == 5:
        house = 'Slytherin'
    elif len(name) == 6:
        house = 'Ravenclaw'
    else:
        house = 'Hufflepuff'

    print(f'{name} goes to {house}.')

    command = input()

if sorting_students:
    print(f'Welcome to Hogwarts.')
