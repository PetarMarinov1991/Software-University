GOAL = 10000

steps = 0
goal_reached = False

while steps < GOAL:
    command = input()

    if command == 'Going home':
        command = input()
        steps += int(command)
        break

    steps += int(command)

if steps >= GOAL:
    goal_reached = True

if goal_reached:
    print(f'Goal reached! Good job!')
else:
    print(f'{GOAL - steps} more steps to reach goal.')
