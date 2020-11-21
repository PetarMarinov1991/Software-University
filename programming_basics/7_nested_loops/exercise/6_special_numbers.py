number = int(input())

for first_digit in range(1, 10):
    for second_digit in range(1, 10):
        for third_digit in range(1, 10):
            for fourth_digit in range(1, 10):

                digits = [first_digit, second_digit, third_digit, fourth_digit]
                evens = [digit for digit in digits if number % digit == 0]

                if len(evens) == 4:
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=' ')
