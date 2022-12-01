snowballs_count = int(input())

output = ''
max_value = 0

for _ in range(snowballs_count):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = int((weight / time) ** quality)

    if value > max_value:
        output = f'{weight} : {time} = {value} ({quality})'
        max_value = value

print(output)
