campaign_days = int(input())
confectioners_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cakes_price = cakes_count * 45
waffles_price = waffles_count * 5.80
pancakes_price = pancakes_count * 3.20

money_per_day = (cakes_price + waffles_price + pancakes_price) * confectioners_count
campaign_money = campaign_days * money_per_day

total_money = campaign_money * 0.875

print(f'{total_money:.2f}')


