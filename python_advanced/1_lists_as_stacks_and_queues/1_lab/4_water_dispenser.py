from collections import deque

water_available = int(input())
queue = deque()

while True:
    name = input()

    if name == 'Start':
        break

    queue.append(name)

while True:
    command = input().split()

    if command[0] == 'End':
        break

    if command[0] == 'refill':
        water_available += int(command[1])
    elif int(command[0]) <= water_available:
        water_available -= int(command[0])
        print(f'{queue.popleft()} got water')
    else:
        print(f'{queue.popleft()} must wait')

print(f'{water_available} liters left')
