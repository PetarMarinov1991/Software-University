player_name = input()

STARTING_POINTS = 301
scored_points = 0
shot_successful = 0
shot_fail = 0

command = input()

while command != 'Retire':
    target = command
    shot_score = int(input())

    if target == 'Single':
        scored_points = shot_score
        if scored_points <= STARTING_POINTS:
            STARTING_POINTS -= scored_points
            shot_successful += 1
        else:
            shot_fail += 1

    elif target == 'Double':
        scored_points = shot_score * 2
        if scored_points <= STARTING_POINTS:
            STARTING_POINTS -= scored_points
            shot_successful += 1
        else:
            shot_fail += 1

    elif target == 'Triple':
        scored_points = shot_score * 3
        if scored_points <= STARTING_POINTS:
            STARTING_POINTS -= scored_points
            shot_successful += 1
        else:
            shot_fail += 1

    if STARTING_POINTS == 0:
        print(f'{player_name} won the leg with {shot_successful} shots.')
        break

    command = input()

    if command == 'Retire':
        print(f'{player_name} retired after {shot_fail} unsuccessful shots.')
        break
