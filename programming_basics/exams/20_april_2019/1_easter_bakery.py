price_kg_flour = float(input())
kg_flour = float(input())
kg_sugar = float(input())
eggs = int(input())
may_packages = int(input())

sugar_price = price_kg_flour * 0.75
eggs_price = price_kg_flour * 1.1
may_price = sugar_price * 0.2

flour_sum = price_kg_flour * kg_flour
eggs_sum = eggs_price * eggs
sugar_sum = sugar_price * kg_sugar
may_sum = may_price * may_packages

total_sum = flour_sum + eggs_sum + sugar_sum + may_sum
print(f'{total_sum:.2f}')
