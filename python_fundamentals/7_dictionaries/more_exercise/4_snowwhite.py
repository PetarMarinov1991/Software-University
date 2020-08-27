from functools import reduce

dwarfs = dict()

while True:
    line = input().split(' <:> ')

    if line[0] == 'Once upon a time':
        break

    name, hat_color, physics = line[0], line[1], int(line[2])

    if hat_color not in dwarfs:
        dwarfs.update({hat_color: {name: physics}})
    elif name not in dwarfs[hat_color]:
        dwarfs[hat_color].update({name: physics})
    elif dwarfs[hat_color][name] < physics:
        dwarfs[hat_color][name] = physics

for color, info in dwarfs.items():
    dwarfs.update({color: list(reduce(lambda x, y: x + y, info.items()))})

dwarfs = {k: v for k, v in sorted(dwarfs.items(), key=lambda x: (-x[1][1], -len(x[1])))}

for color, info in dwarfs.items():
    while info:
        print(f'({color}) {info.pop(0)} <-> {info.pop(0)}')
