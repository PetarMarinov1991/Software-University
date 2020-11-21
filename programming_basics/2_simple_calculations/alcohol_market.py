whiskey_price = float(input())
liters_beer = float(input())
liters_wine = float(input())
liters_rakia = float(input())
liters_whiskey = float(input())

rakia_price = whiskey_price * 0.5
wine_price = rakia_price * 0.6
beer_price = rakia_price * 0.2

total_sum = whiskey_price * liters_whiskey + rakia_price * liters_rakia + wine_price * liters_wine + beer_price * liters_beer

print(f'{total_sum:.2f}')
