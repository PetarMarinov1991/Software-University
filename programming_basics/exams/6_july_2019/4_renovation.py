from math import ceil

wall_height = int(input())
wall_width = int(input())
percentage = int(input())

walls = wall_height * wall_width * 4
walls = int(ceil(walls - (walls / 100 * percentage)))

command = input()

while command != 'Tired!':
    liters_paint = int(command)

    walls -= liters_paint

    if walls <= 0:
        break

    command = input()

if walls > 0:
    print(f'{walls} quadratic m left.')
elif walls == 0:
    print('All walls are painted! Great job, Pesho!')
else:
    print(f'All walls are painted and you have {abs(walls)} l paint left!')

