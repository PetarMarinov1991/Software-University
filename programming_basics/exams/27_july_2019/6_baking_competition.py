bakers_count = int(input())

cookies_count = 0
cakes_count = 0
waffles_count = 0

for baker in range(bakers_count):
    baker_cookies_count = 0
    baker_cakes_count = 0
    baker_waffles_count = 0

    baker_name = input()
    sweetie = input()

    while sweetie != 'Stop baking!':
        sweetie_count = int(input())

        if sweetie == 'cookies':
            cookies_count += sweetie_count
            baker_cookies_count += sweetie_count
        elif sweetie == 'cakes':
            cakes_count += sweetie_count
            baker_cakes_count += sweetie_count
        elif sweetie == 'waffles':
            waffles_count += sweetie_count
            baker_waffles_count += sweetie_count

        sweetie = input()

    print(f'{baker_name} baked {baker_cookies_count} cookies, {baker_cakes_count} cakes and {baker_waffles_count} waffles.')

all_bakery_count = cookies_count + cakes_count + waffles_count
sum_for_charity = cookies_count * 1.50 + cakes_count * 7.80 + waffles_count * 2.30

print(f'All bakery sold: {all_bakery_count}')
print(f'Total sum for charity: {sum_for_charity:.2f} lv.')
