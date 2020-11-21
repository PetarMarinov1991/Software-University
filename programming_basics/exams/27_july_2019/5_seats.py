
tickets = int(input())

for i in range(tickets):
    ticket_number = input()

    letter_1 = ticket_number[0]
    letter_2 = ticket_number[1]
    letter_3 = ticket_number[2]
    letter_4 = ticket_number[3]

    if len(ticket_number) == 4:
        if ord(letter_1) in range(65, 90):
            print(f'Seat decoded: {letter_1}{letter_2}{letter_3}')
        else:
            print(f'Seat decoded: {letter_4}{letter_2}{letter_3}')

    elif len(ticket_number) == 5 or 6:
        letter_2 = ord(letter_2)
        print(f'Seat decoded: {letter_1}{letter_2}')

