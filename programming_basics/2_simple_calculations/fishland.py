mackerel_price = float(input())
sprat_price = float(input())
kg_palm = float(input())
kg_horse_mackerel = float(input())
kg_clams = float(input())

palm_price = kg_palm * mackerel_price * 1.6
horse_mackerel_price = kg_horse_mackerel * sprat_price * 1.8
clams_price = kg_clams * 7.50

total_price = palm_price + horse_mackerel_price + clams_price

print(f'{total_price:.2f}')
