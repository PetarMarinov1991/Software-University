from math import ceil

guests = int(input())
budget = int(input())

easter_bread = ceil(guests / 3)
eggs = guests * 2

easter_bread_price = easter_bread * 4
eggs_price = eggs * 0.45
total_sum = easter_bread_price + eggs_price

diff = abs(budget - total_sum)

if total_sum <= budget:
    print(f'Lyubo bought {easter_bread} Easter bread and {eggs} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    print(f'Lyubo doesn\'t have enough money.')
    print(f'He needs {diff:.2f} lv. more.')
