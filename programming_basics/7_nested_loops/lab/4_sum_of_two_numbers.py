start = int(input())
end = int(input())
magic_number = int(input())

counter = 0

for a in range(start, end + 1):
    for b in range(start, end + 1):
        result = a + b
        counter += 1
        if result == magic_number:
            print(f'Combination N:{counter} ({a} + {b} = {magic_number})')
            exit(0)

print(f'{counter} combinations - neither equals {magic_number}')
