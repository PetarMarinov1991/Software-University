budget = float(input())
kg_flour_price = float(input())

pack_eggs_price = 0.75 * kg_flour_price
liter_milk_price = 1.25 * kg_flour_price
milk_250_ml_price = liter_milk_price / 4
easter_bread_price = kg_flour_price + pack_eggs_price + milk_250_ml_price

easter_bread_count = 0
eggs_count = 0

while budget >= easter_bread_price:
    budget -= easter_bread_price
    easter_bread_count += 1
    eggs_count += 3

    if easter_bread_count % 3 == 0:
        eggs_count -= easter_bread_count - 2

print(f'You made {easter_bread_count} cozonacs! Now you have {eggs_count} eggs and {budget:.2f}BGN left.')
