chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

chicken_price = 10.35
fish_price = 12.40
vegetarian_price = 8.15
bill = chicken_menu * chicken_price + fish_menu * fish_price + vegetarian_menu * vegetarian_price
desert = bill * 0.2
delivery = 2.50

total = bill + desert + delivery
print(f'Total: {total:.2f}')
