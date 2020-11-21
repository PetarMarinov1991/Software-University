start = input()
end = input()
forbidden = input()

combination_count = 0

for first_letter in range(ord(start), ord(end) + 1):
    for second_letter in range(ord(start), ord(end) + 1):
        for third_letter in range(ord(start), ord(end) + 1):
            combination = f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}'

            if forbidden not in combination:
                combination_count += 1
                print(f'{combination}', end=' ')

print(combination_count)
