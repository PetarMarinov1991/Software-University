egg_size = input()
egg_colour = input()
egg_batches = int(input())

egg_paint_price = 0

if egg_size == 'Large':
    if egg_colour == 'Red':
        egg_paint_price = 16
    elif egg_colour == 'Green':
        egg_paint_price = 12
    elif egg_colour == 'Yellow':
        egg_paint_price = 9

elif egg_size == 'Medium':
    if egg_colour == 'Red':
        egg_paint_price = 13
    elif egg_colour == 'Green':
        egg_paint_price = 9
    elif egg_colour == 'Yellow':
        egg_paint_price = 7

elif egg_size == 'Small':
    if egg_colour == 'Red':
        egg_paint_price = 9
    elif egg_colour == 'Green':
        egg_paint_price = 8
    elif egg_colour == 'Yellow':
        egg_paint_price = 5

total_price = egg_paint_price * egg_batches * 0.65

print(f'{total_price:.2f} leva.')
