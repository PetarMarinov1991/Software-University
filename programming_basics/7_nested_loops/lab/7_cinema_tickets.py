command = input()

student = 0
standard = 0
kid = 0
tickets = 0

while command != 'Finish':
    movie_name = command
    empty_seats = int(input())

    for movie in range(empty_seats):
        ticket = input()

        if ticket == 'End':
            break

        if ticket == 'student':
            student += 1
        elif ticket == 'standard':
            standard += 1
        elif ticket == 'kid':
            kid += 1

        tickets += 1

    print(f'{movie_name} - {tickets / empty_seats * 100:.2f}% full.')
    tickets = 0

    command = input()

total_tickets = student + standard + kid

print(f'Total tickets: {total_tickets}')
print(f'{student / total_tickets * 100:.2f}% student tickets.')
print(f'{standard / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid / total_tickets * 100:.2f}% kids tickets.')
