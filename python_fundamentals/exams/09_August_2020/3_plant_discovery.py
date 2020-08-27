def valid_plant(my_plant, my_plants):
    if my_plant in my_plants:
        return True
    else:
        print('error')


plants = dict()

for _ in range(int(input())):
    line = input().split('<->')
    name, rarity = line[0], int(line[1])

    if name not in plants:
        plants[name] = [0, []]
    plants[name][0] = rarity

while True:
    line = input().split(': ')
    command = line[0]

    if command == 'Exhibition':
        break

    if command == 'Rate':
        name, rating = line[1].split(' - ')
        if valid_plant(name, plants):
            plants[name][1].append(int(rating))
    elif command == 'Update':
        name, new_rarity = line[1].split(' - ')
        if valid_plant(name, plants):
            plants[name][0] = int(new_rarity)
    elif command == 'Reset':
        name = line[1]
        if valid_plant(name, plants):
            plants[name][1] = [0]

for name, stats in plants.items():
    if len(stats[1]) > 0 and sum(stats[1]) > 0:
        stats[1] = sum(stats[1]) / (len(stats[1]))
    else:
        stats[1] = 0

plants = {k: v for k, v in sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1]))}

print('Plants for the exhibition:')
for name, stats in plants.items():
    print(f'- {name}; Rarity: {stats[0]}; Rating: {stats[1]:.2f}')
