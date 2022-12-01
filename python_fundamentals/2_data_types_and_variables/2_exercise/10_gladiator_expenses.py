lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_breaks = 0

for fight_number in range(1, lost_fights_count + 1):
    if fight_number % 2 == 0:
        expenses += helmet_price
    if fight_number % 3 == 0:
        expenses += sword_price
        if fight_number % 2 == 0:
            expenses += shield_price
            shield_breaks += 1
            if shield_breaks == 2:
                expenses += armor_price
                shield_breaks = 0

print(f'Gladiator expenses: {expenses:.2f} aureus')
