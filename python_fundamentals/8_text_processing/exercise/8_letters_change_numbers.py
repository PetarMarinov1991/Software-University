text = input().split()

alphabet = "-abcdefghijklmnopqrstuvwxyz"
position = dict([(x[1], x[0]) for x in enumerate(alphabet)])

final_result = 0

for element in text:
    result = 0
    number = int(element[1:-1])

    if element[0].isupper():
        result = number / position[element[0].lower()]
    elif element[0].islower():
        result = number * position[element[0]]

    if element[-1].isupper():
        result -= position[element[-1].lower()]
    elif element[-1].islower():
        result += position[element[-1]]

    final_result += result

print(f'{round(final_result, 2):.2f}')
