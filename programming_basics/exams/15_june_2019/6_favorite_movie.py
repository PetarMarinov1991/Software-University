command = input()

movies_checked = 0
current_score = 0
biggest_score = 0
biggest_title = ''

while command != 'STOP':
    movie_title = command
    current_score = 0
    movies_checked += 1

    if movies_checked == 7:
        print('The limit is reached.')
        print(f'The best movie for you is {biggest_title} with {biggest_score} ASCII sum.')
        break

    for index in range(len(movie_title)):
        value = (ord(movie_title[index]))

        if 65 <= value <= 90:
            value -= len(movie_title)
        elif 97 <= value <= 122:
            value -= len(movie_title) * 2

        current_score += value

        if current_score > biggest_score:
            biggest_score = current_score
            biggest_title = movie_title

    command = input()

    if command == 'STOP':
        print(f'The best movie for you is {biggest_title} with {biggest_score} ASCII sum.')
