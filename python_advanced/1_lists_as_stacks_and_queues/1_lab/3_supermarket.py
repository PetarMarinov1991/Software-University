from collections import deque

queue = deque()

while True:
    name = input()

    if name == 'End':
        break

    if name == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(name)

print(f'{len(queue)} people remaining.')
