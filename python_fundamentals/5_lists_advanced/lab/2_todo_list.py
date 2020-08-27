todo = []

while True:
    command = input().split('-')

    if command[0] == 'End':
        break

    todo += [command[0] + command[1]]

result = []
last_priority = []

for item in sorted(todo):
    if '10' in item:
        last_priority.append(item[2:])
    else:
        result.append(item[1:])

print(result + last_priority)
