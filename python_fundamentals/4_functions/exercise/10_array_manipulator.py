def even(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    return evens


def odd(numbers):
    odds = [x for x in numbers if x % 2 == 1]
    return odds


def exchange(idx):
    global numbers
    idx = int(command[1])
    if idx < 0 or idx > len(numbers):
        print('Invalid index')
    else:
        numbers = numbers[idx + 1:] + numbers[:idx + 1]


def max_or_min(numbers):
    if command[1] == 'even':
        if len(even(numbers)) == 0:
            return 'No matches'
        best_number = even(numbers)[0]
    else:
        if len(odd(numbers)) == 0:
            return 'No matches'
        best_number = odd(numbers)[0]

    best_index = 0

    if command[0] == 'max':
        for i in range(len(numbers)):
            current = numbers[i]
            if command[1] == 'even':
                if current >= best_number and current % 2 == 0:
                    best_number = current
                    best_index = i
            else:
                if current >= best_number and current % 2 == 1:
                    best_number = current
                    best_index = i
        return best_index

    elif command[0] == 'min':
        for i in range(len(numbers)):
            current = numbers[i]
            if command[1] == 'even':
                if current <= best_number and current % 2 == 0:
                    best_number = current
                    best_index = i
            else:
                if current <= best_number and current % 2 == 1:
                    best_number = current
                    best_index = i
        return best_index


def first_or_last(numbers):
    if int(command[1]) > len(numbers):
        return 'Invalid count'

    if command[2] == 'even':
        if not even(numbers):
            return '[]'
        elif command[0] == 'first':
            return even(numbers)[:int(command[1])]
        elif command[0] == 'last':
            return even(numbers)[-int(command[1]):]

    elif command[2] == 'odd':
        if not odd(numbers):
            return '[]'
        elif command[0] == 'first':
            return odd(numbers)[:int(command[1])]
        elif command[0] == 'last':
            return odd(numbers)[-int(command[1]):]


numbers = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == 'end':
        break

    if command[0] == 'exchange':
        exchange(command[1])
    elif command[0] in ['max', 'min']:
        print(max_or_min(numbers))
    elif command[0] in ['first', 'last']:
        print(first_or_last(numbers))

print(numbers)
