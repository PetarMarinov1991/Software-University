student_tickets = 0
standard_tickets = 0
kids_tickets = 0
current_movie_tickets = 0
total_tickets = 0

current_movie = ''

command = input()

while command != 'Finish':
    movie_name = command
    free_seats = int(input())

    for seats in range(1, free_seats + 1):
        ticket_type = input()

        if ticket_type == 'student':
            student_tickets += 1
            current_movie_tickets += 1
            total_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
            current_movie_tickets += 1
            total_tickets += 1
        elif ticket_type == 'kid':
            kids_tickets += 1
            current_movie_tickets += 1
            total_tickets += 1

        if ticket_type == 'End' or free_seats == current_movie_tickets:
            seats_taken = (current_movie_tickets / free_seats) * 100
            current_movie = movie_name
            print(f'{current_movie} - {seats_taken:.2f}% full.')
            current_movie_tickets = 0
            break

    command = input()

    if command == 'Finish':
        average_student_tickets = (student_tickets / total_tickets) * 100
        average_standard_tickets = (standard_tickets / total_tickets) * 100
        average_kids_tickets = (kids_tickets / total_tickets) * 100

        print(f'Total tickets: {total_tickets}')
        print(f'{average_student_tickets:.2f}% student tickets.')
        print(f'{average_standard_tickets:.2f}% standard tickets.')
        print(f'{average_kids_tickets:.2f}% kids tickets.')

