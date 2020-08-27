from collections import deque

clothes = deque([int(x) for x in input().split()])
capacity = int(input())

racks = 0
clothes_sum = 0
while clothes:
    if clothes_sum + clothes[0] <= capacity:
        clothes_sum += clothes.popleft()
    else:
        racks += 1
        clothes_sum = 0

if clothes_sum > 0:
    racks += 1

print(racks)
