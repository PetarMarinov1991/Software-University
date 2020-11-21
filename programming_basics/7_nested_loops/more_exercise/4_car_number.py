start = int(input())
end = int(input())

for first_digit in range(start, end + 1):
    for second_digit in range(start, end + 1):
        for third_digit in range(start, end + 1):
            for fourth_digit in range(start, end + 1):

                condition_1 = first_digit > fourth_digit
                condition_2 = (second_digit + third_digit) % 2 == 0
                condition_3 = first_digit % 2 == 0 and fourth_digit % 2 == 1
                condition_4 = first_digit % 2 == 1 and fourth_digit % 2 == 0

                if (condition_3 or condition_4) and condition_1 and condition_2:
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=' ')
