price_kg_vegetables = float(input())
price_kg_fruits = float(input())
kg_vegetables = float(input())
kg_fruits = float(input())

price_vegetables = price_kg_vegetables * kg_vegetables
price_fruits = price_kg_fruits * kg_fruits

total_price = (price_vegetables + price_fruits) / 1.94

print(f'{total_price:.2f}')
