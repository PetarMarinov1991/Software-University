import re

regex = r"([A-Za-z0-9!@#$?]+)=(\d+)<<(.+)"

while True:
    line = input()

    if line == 'Last note':
        break

    data = re.findall(regex, line)
    name = ''

    if '=' in line:
        name, _ = line.split('=')

    if data:
        for match in data:
            peak, length, coordinates = match[0], int(match[1]), match[2]
            if peak == name and length == len(coordinates):
                current_peak = ''
                for char in peak:
                    if char.isalpha():
                        current_peak += char
                print(f'Coordinates found! {current_peak} -> {coordinates}')
            else:
                print('Nothing found!')
    else:
        print('Nothing found!')
