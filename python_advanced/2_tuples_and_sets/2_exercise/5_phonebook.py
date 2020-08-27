phonebook = dict()
count = 0

while True:
    line = input().split('-')

    if len(line) == 1:
        count = int(line[0])
        break

    name, phone = line[0], line[1]
    if name not in phonebook:
        phonebook[name] = ''
    phonebook[name] = phone

for _ in range(count):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
