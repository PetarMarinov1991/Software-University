command = input()

points = 0
most_points = 0
winner = ''

while command != 'Stop':
    player_name = command
    points = 0

    for index in range(len(player_name)):
        number = int(input())
        letter = ord(player_name[index])

        if letter == number:
            points += 10
        else:
            points += 2

        if points >= most_points:
            most_points = points
            winner = player_name

    command = input()

    if command == 'Stop':
        print(f'The winner is {winner} with {most_points} points!')

