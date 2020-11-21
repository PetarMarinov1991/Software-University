eggs_count = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

max_colour = ''

for eggs in range(eggs_count):
    colour = input()

    if colour == 'red':
        red_eggs += 1
    elif colour == 'orange':
        orange_eggs += 1
    elif colour == 'blue':
        blue_eggs += 1
    elif colour == 'green':
        green_eggs += 1

list_eggs = [red_eggs, orange_eggs, blue_eggs, green_eggs]

if max(list_eggs) == red_eggs:
    max_colour = 'red'
elif max(list_eggs) == orange_eggs:
    max_colour = 'orange'
elif max(list_eggs) == blue_eggs:
    max_colour = 'blue'
elif max(list_eggs) == green_eggs:
    max_colour = 'green'

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')
print(f'Max eggs: {max(list_eggs)} -> {max_colour}')
