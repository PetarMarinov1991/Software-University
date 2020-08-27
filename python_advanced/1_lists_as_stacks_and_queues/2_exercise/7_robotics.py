from collections import deque


def next_second(h, m, s):
    return s + m * 60 + h * 3600 + 1


def time_to_hours(s):
    s = s % (24 * 3600)
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60

    return f'[{h:02d}:{m:02d}:{s:02d}]'


robots = deque(input().split(';'))
hours, minutes, secs = [int(x) for x in input().split(':')]
seconds = next_second(hours, minutes, secs)
robots_time = dict()
products = deque()

while True:
    product = input()

    if product == 'End':
        break

    products.append(product)

while products:
    name, work_time = '', 0
    available = False
    for robot in robots:
        name, work_time = robot.split('-')
        if name not in robots_time:
            robots_time[name] = seconds
        if robots_time[name] == seconds:
            available = True
            break
    current_product = products.popleft()
    if available:
        print(f'{name} - {current_product} {time_to_hours(robots_time[name])}')
        robots_time[name] += int(work_time)
    else:
        products.append(current_product)
    robots.append(robots.popleft())
    seconds += 1
