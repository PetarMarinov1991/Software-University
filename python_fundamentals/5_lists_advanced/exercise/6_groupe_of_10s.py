numbers = list(map(int, input().split(', ')))

group = 10

while numbers:
    result = [num for num in numbers if num <= group]
    print(f'Group of {group}\'s: {result}')

    for num in result:
        numbers.remove(num)

    group += 10
    result.clear()
