points = int(input())

bonus_points = 0

if points > 1000:
    bonus_points += points * 0.1
elif points > 100:
    bonus_points += points * 0.2
else:
    bonus_points += 5

extra_points = 0

if points % 2 == 0:
    extra_points += 1
elif points % 10 == 5:
    extra_points += 2

total_bonus = bonus_points + extra_points
final_score = points + total_bonus

print(total_bonus)
print(final_score)
