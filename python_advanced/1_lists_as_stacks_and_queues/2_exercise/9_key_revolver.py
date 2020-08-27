from collections import deque

bullet_price = int(input())
barrel = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
money = int(input())

shots = 0
current_barrel = barrel

while bullets:
    if current_barrel == 0:
        print('Reloading!')
        current_barrel = barrel

    if not locks:
        break

    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet > current_lock:
        print('Ping!')
        locks.insert(0, current_lock)
    else:
        print('Bang!')
    current_barrel -= 1
    shots += 1

if not locks:
    print(f'{len(bullets)} bullets left. Earned ${money - bullet_price * shots}')
else:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')
