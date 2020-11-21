cinema_capacity = int(input())

ticket_price = 5
bill = 0

command = input()

while command != 'Movie time!':
    people = int(command)
    cinema_capacity -= people

    if cinema_capacity < 0:
        print(f'The cinema is full.')
        print(f'Cinema income - {bill} lv.')
        break

    bill += people * ticket_price

    if people % 3 == 0:
        bill -= 5

    command = input()

    if command == 'Movie time!':
        print(f'There are {cinema_capacity} seats left in the cinema.')
        print(f'Cinema income - {bill} lv.')
