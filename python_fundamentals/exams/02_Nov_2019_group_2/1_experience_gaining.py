amount_experience = int(input())
battles = int(input())

for i in range(1, battles + 1):
    current_battle = int(input())

    if i % 3 == 0:
        current_battle *= 1.15
    if i % 5 == 0:
        current_battle *= 0.9

    amount_experience -= current_battle

    if amount_experience <= 0:
        print(f'Player successfully collected his needed experience for {i} battles.')
        break

if amount_experience > 0:
    print(f'Player was not able to collect the needed experience, {amount_experience:.2f} more needed.')
