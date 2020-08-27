bands = dict()
play = dict()

while True:
    line = input().split('; ')
    command = line[0]

    if command == 'start of concert':
        last_band = input()
        break

    band_name = line[1]
    if command == 'Add':
        members = line[2].split(', ')
        if band_name not in bands:
            bands[band_name] = []
        bands[band_name] += [member for member in members if member not in bands[band_name]]
    elif command == 'Play':
        time = int(line[2])
        if band_name not in play:
            play[band_name] = 0
        play[band_name] += time

print(f'Total time: {sum(play.values())}')
play = {k: v for k, v in sorted(play.items(), key=lambda x: (-x[1], x[0]))}
for band, time in play.items():
    print(f'{band} -> {time}')
if last_band:
    print(f'{last_band}')
    for member in bands[last_band]:
        print(f'=> {member}')
