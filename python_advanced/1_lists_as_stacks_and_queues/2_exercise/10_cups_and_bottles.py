from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

wasted_water = 0

while bottles:

    if not cups:
        print(f'Bottles: {" ".join([str(x) for x in bottles])}')
        break

    current_bottle = bottles.pop()
    current_cup = cups.popleft()

    cups.insert(0, current_cup - current_bottle)
    if cups[0] <= 0:
        wasted_water += abs(cups[0])
        cups.popleft()

if not bottles:
    print(f'Cups: {" ".join([str(x) for x in cups])}')
print(f'Wasted litters of water: {wasted_water}')
