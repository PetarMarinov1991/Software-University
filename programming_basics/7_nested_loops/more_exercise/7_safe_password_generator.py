def password_generator(value_1, value_2, combo):
    combinations = 0

    for first_symbol in range(35, 55 + 1):
        for second_symbol in range(64, 96 + 1):
            for first_digit in range(1, end_first + 1):
                for second_digit in range(1, end_second + 1):
                    print(f'{chr(first_symbol)}{chr(second_symbol)}{first_digit}{second_digit}'
                          f'{chr(second_symbol)}{chr(first_symbol)}', end='|')

                    combinations += 1

                    if combinations == max_generated or (first_digit == end_first and second_digit == end_second):
                        exit(0)

                    first_symbol += 1
                    second_symbol += 1

                    if first_symbol > 55:
                        first_symbol = 35

                    if second_symbol > 96:
                        second_symbol = 64


end_first = int(input())
end_second = int(input())
max_generated = int(input())

print(password_generator(end_first, end_second, max_generated))
