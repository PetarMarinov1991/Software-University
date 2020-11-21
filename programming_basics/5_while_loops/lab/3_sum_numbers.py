command = input()

sum_numbers = 0

while command != 'Stop':
    num = int(command)
    sum_numbers += num

    command = input()

print(sum_numbers)
