from collections import deque

stack = deque()

for _ in range(int(input())):
    line = [int(x) for x in input().split()]
    command = line[0]

    if command == 1:
        stack.insert(0, line[1])
    elif stack:
        if command == 2:
            stack.popleft()
        elif command == 3:
            print(max(stack))
        elif command == 4:
            print(min(stack))

print(', '.join([str(x) for x in stack]))
