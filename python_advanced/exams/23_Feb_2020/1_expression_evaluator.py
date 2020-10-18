from collections import deque

expression = deque(input().split())

numbers = []
result = 0

while expression:
    char = expression.popleft()
    numbers.append(char)
    if char in ['*', '/', '+', '-']:
        if len(numbers) == 2:
            evaluation = eval(f'{result}{char}{numbers[0]}')
        else:
            if char in ['*', '/']:
                if result == 0:
                    result = 1
            if result != 0:
                evaluation = eval(f'{result}{char}{numbers[0]}{char}{numbers[1]}')
            else:
                evaluation = eval(f'{numbers[0]}{char}{numbers[1]}')
        result = int(evaluation)
        numbers = []

print(result)
