budget = float(input())
kg_flour = float(input())

pack_eggs = 0.75 * kg_flour
milk = 1.25 * kg_flour
cozonac_price = pack_eggs + kg_flour + milk / 4

colored_eggs = 0
cozonacs_made = 0

while budget >= cozonac_price:
    budget -= cozonac_price
    cozonacs_made += 1
    colored_eggs += 3

    if cozonacs_made % 3 == 0:
        colored_eggs -= cozonacs_made - 2

print(f'You made {cozonacs_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
