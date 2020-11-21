import sys

max_number = -sys.maxsize - 1
min_number = sys.maxsize

n = int(input())

current_number = 0

for i in range(n):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
