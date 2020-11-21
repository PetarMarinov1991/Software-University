import math

series_title = input()
episode_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration / 8
rest_duration = break_duration / 4
time_left = break_duration - (lunch_duration + rest_duration)

diff = math.ceil(abs(time_left - episode_duration))

if time_left >= episode_duration:
    print(f'You have enough time to watch {series_title} and left with {diff} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {series_title}, you need {diff} more minutes.')
