days = int(input())
players = int(input())
energy = float(input())
water = days * players * float(input())
food = days * players * float(input())

for day in range(1, days + 1):
    energy -= float(input())

    if energy <= 0:
        break
    if day % 2 == 0:
        energy *= 1.05
        water *= 0.7
    if day % 3 == 0:
        food -= food / players
        energy *= 1.1

if energy > 0:
    print(f'You are ready for the quest. You will be left with - {energy:.2f} energy!')
else:
    print(f'You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.')
