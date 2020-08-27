mine = dict()

while True:
    ruin = input()

    if ruin == 'stop':
        break

    quantity = int(input())

    if ruin not in mine:
        mine.update({ruin: quantity})
    else:
        mine[ruin] += quantity

for ruin, quantity in mine.items():
    print(f'{ruin} -> {quantity}')
