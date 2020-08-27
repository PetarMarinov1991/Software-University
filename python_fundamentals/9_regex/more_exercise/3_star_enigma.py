import re

attacked_planets = []
destroyed_planets = []

for _ in range(int(input())):
    count_letter = 0
    encrypted = ''

    message = input()

    for char in message.lower():
        if char in ['s', 't', 'a', 'r']:
            count_letter += 1

    for char in message:
        encrypted += chr(ord(char) - count_letter)

    delimiters = '@', ':', '!', '->'
    regex = '|'.join(map(re.escape, delimiters))
    data = [element for element in re.split(regex, encrypted)[1:] if element]

    planet = ''.join([char for char in data[0] if char.isalpha()])
    population = ''.join([char for char in data[1] if char.isdigit()])
    attack = ''.join([char for char in data[2] if char == 'A' or char == 'D'])
    soldiers = ''.join([char for char in data[3] if char.isdigit()])

    if planet and population and attack and soldiers:
        if attack == 'A':
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)

print(f'Attacked planets: {len(attacked_planets)}')
for planet in sorted(attacked_planets):
    print(f'-> {planet}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in sorted(destroyed_planets):
    print(f'-> {planet}')
