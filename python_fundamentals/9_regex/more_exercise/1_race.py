names = input().split(', ')

racers = dict()

for name in names:
    racers.update({name: 0})

while True:
    name = ''
    distance_ran = 0

    text = input()

    if text == 'end of race':
        break

    for char in text:
        if char.isalpha():
            name += char
        elif char.isdigit():
            distance_ran += int(char)

    if name in racers:
        racers[name] += distance_ran

racers = {k: v for k, v in sorted(racers.items(), key=lambda x: -x[1])}
top_3 = [racer for racer, distance_ran in racers.items()][:3]

print(f'1st place: {top_3[0]}')
print(f'2nd place: {top_3[1]}')
print(f'3rd place: {top_3[2]}')
