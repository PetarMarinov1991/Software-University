easter_breads_count = int(input())

grade = 0
max_grade = 0
best_baker = ''

for easter_breads in range(easter_breads_count):
    new_best_baker = False
    grade = 0

    baker_name = input()

    while True:
        command = input()

        if command == 'Stop':
            break

        grade += int(command)

        if grade > max_grade:
            max_grade = grade
            best_baker = baker_name
            new_best_baker = True

    print(f'{baker_name} has {grade} points.')

    if new_best_baker:
        print(f'{best_baker} is the new number 1!')

print(f'{best_baker} won competition with {max_grade} points!')
