budget = float(input())
kg_flour_price = float(input())

bread_price = kg_flour_price + 0.75 * kg_flour_price + 1.25 * kg_flour_price / 4
colored_eggs = 0
bread_count = 0

while budget >= bread_price:
    budget -= bread_price
    bread_count += 1
    colored_eggs += 3

    if bread_count % 3 == 0:
        colored_eggs -= bread_count - 2

print(f'You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
