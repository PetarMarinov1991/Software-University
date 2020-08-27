from collections import deque

kids = deque(input().split())
toss = int(input())

while len(kids) > 1:
    for i in range(toss):
        kids.append(kids.popleft())
        if i == toss - 1:
            print(f'Removed {kids.pop()}')
            i = 0
print(f'Last is {kids.pop()}')
