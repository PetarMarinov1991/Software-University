chrysanthemum_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()

chrysanthemum_price = 0
roses_price = 0
tulips_price = 0

if season == 'Spring' or season == 'Summer':
    chrysanthemum_price = 2
    roses_price = 4.1
    tulips_price = 2.5
elif season == 'Autumn' or season == 'Winter':
    chrysanthemum_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15

flowers_price = chrysanthemum_price * chrysanthemum_count + roses_price * roses_count + tulips_price * tulips_count
flowers_count = chrysanthemum_count + roses_count + tulips_count

if is_holiday == 'Y':
    flowers_price += flowers_price * 0.15

if tulips_count > 7 and season == 'Spring':
    flowers_price -= flowers_price * 0.05
elif roses_count >= 10 and season == 'Winter':
    flowers_price -= flowers_price * 0.1

if flowers_count > 20:
    flowers_price -= flowers_price * 0.2

print(f'{flowers_price + 2:.2f}')
