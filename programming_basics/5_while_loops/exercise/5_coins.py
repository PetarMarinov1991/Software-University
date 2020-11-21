import math

change = float(input())
coins = 0
change *= 100

while change > 0:
    if change >= 200:
        coins += 1
        change -= 200
    elif change >= 100:
        coins += 1
        change -= 100
    elif change >= 50:
        coins += 1
        change -= 50
    elif change >= 20:
        coins += 1
        change -= 20
    elif change >= 10:
        coins += 1
        change -= 10
    elif change >= 5:
        coins += 1
        change -= 5
    elif change >= 2:
        coins += 1
        change -= 2
    else:
        coins += 1
        change -= 1

    change = math.floor(change)
print(coins)
