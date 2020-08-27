numbers = input().split()

race_track = [int(num) for num in numbers]
left_racer = race_track[:(len(race_track) - 1) // 2]
right_racer = race_track[(len(race_track) + 1) // 2:][::-1]

time_left = 0
for time in left_racer:
    if time == 0:
        time_left *= 0.8
    else:
        time_left += time

time_right = 0
for time in right_racer:
    if time == 0:
        time_right *= 0.8
    else:
        time_right += time

if time_left <= time_right:
    print(f'The winner is left with total time: {time_left:.1f}')
else:
    print(f'The winner is right with total time: {time_right:.1f}')
