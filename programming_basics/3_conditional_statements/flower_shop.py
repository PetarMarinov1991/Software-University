import math

magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_price = float(input())

magnolia_price = magnolia_count * 3.25
hyacinth_price = hyacinth_count * 4
rose_price = rose_count * 3.50
cactus_price = cactus_count * 8
profit = (magnolia_price + hyacinth_price + rose_price + cactus_price) * 0.95

diff = profit - gift_price

if diff >= 0:
    print(f'She is left with {math.floor(diff)} leva.')
else:
    print(f'She will have to borrow {abs(math.floor(diff))} leva.')
