lines = int(input())

numbers = []
filtered_numbers = []

for i in range(lines):
    num = int(input())
    numbers.append(num)

command = input()

if command == 'positive':
    for number in numbers:
        if number >= 0:
            filtered_numbers.append(number)
elif command == 'negative':
    for number in numbers:
        if number < 0:
            filtered_numbers.append(number)
elif command == 'even':
    for number in numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
elif command == 'odd':
    for number in numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)


print(filtered_numbers)
