detergent = int(input())
detergent_ml = detergent * 750

dishes = 0
pots = 0

counter = 0

while detergent_ml >= 0:
    command = input()
    counter += 1
    if counter % 3 == 0 and command != 'End':
        pots += int(command)
        detergent_ml -= int(command) * 15
    elif command != 'End':
        dishes += int(command)
        detergent_ml -= int(command) * 5
    elif command == 'End':
        break

if detergent_ml >= 0:
    print(f'Detergent was enough!')
    print(f'{dishes} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {detergent_ml} ml.')
else:
    print(f'Not enough detergent, {abs(detergent_ml)} ml. more necessary!')
