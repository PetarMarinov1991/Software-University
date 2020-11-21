kg_skumria_price = float(input())
kg_tsatsa_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

kg_palamud_price = kg_skumria_price * 1.6
kg_safrid_price = kg_tsatsa_price * 1.8

sum_palamud = palamud_kg * kg_palamud_price
sum_safrid = safrid_kg * kg_safrid_price
sum_mussels = mussels_kg * 7.50

total_sum = sum_palamud + sum_safrid + sum_mussels
print(f'{total_sum:.2f}')
