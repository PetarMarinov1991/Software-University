from math import ceil

people = int(input())
entrance_tax = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

sum_for_entrance = people * entrance_tax
sunbeds_count = ceil(people * 0.75)
sum_for_sunbeds = sunbeds_count * sunbed_price
umbrellas_count = ceil(people * 0.50)
sum_for_umbrellas = umbrellas_count * umbrella_price

total_sum = sum_for_entrance + sum_for_sunbeds + sum_for_umbrellas

print(f'{total_sum:.2f} lv.')
