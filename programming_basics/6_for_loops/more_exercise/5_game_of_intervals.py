moves = int(input())

points = 0

range_0_9 = 0
range_10_19 = 0
range_20_29 = 0
range_30_39 = 0
range_40_50 = 0
invalid = 0

for i in range(moves):
    num = int(input())

    if 0 <= num <= 9:
        points += num * 0.2
        range_0_9 += 1
    elif 10 <= num <= 19:
        points += num * 0.3
        range_10_19 += 1
    elif 20 <= num <= 29:
        points += num * 0.4
        range_20_29 += 1
    elif 30 <= num <= 39:
        points += 50
        range_30_39 += 1
    elif 40 <= num <= 50:
        points += 100
        range_40_50 += 1
    else:
        points /= 2
        invalid += 1


percentage_0_9 = range_0_9 / moves * 100
percentage_10_19 = range_10_19 / moves * 100
percentage_20_29 = range_20_29 / moves * 100
percentage_30_39 = range_30_39 / moves * 100
percentage_40_50 = range_40_50 / moves * 100
percentage_invalid = invalid / moves * 100

print(f'{points:.2f}')
print(f'From 0 to 9: {percentage_0_9:.2f}%')
print(f'From 10 to 19: {percentage_10_19:.2f}%')
print(f'From 20 to 29: {percentage_20_29:.2f}%')
print(f'From 30 to 39: {percentage_30_39:.2f}%')
print(f'From 40 to 50: {percentage_40_50:.2f}%')
print(f'Invalid numbers: {percentage_invalid:.2f}%')
