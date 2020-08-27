num_of_lines = int(input())

ascii_sum = 0

for i in range(num_of_lines):
    letter = input()
    ascii_value = ord(letter)
    ascii_sum += ascii_value

print(f'The sum equals: {ascii_sum}')
