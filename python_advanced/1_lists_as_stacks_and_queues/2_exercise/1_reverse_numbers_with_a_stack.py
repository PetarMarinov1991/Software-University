from collections import deque

numbers = deque([int(x) for x in input().split()])

for i in range(len(numbers)):
    numbers.insert(i, numbers.pop())

print(' '.join([str(x) for x in numbers]))
