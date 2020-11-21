rest_days = int(input())

work_days = 365 - rest_days
norm_play_time = 30000
play_time = work_days * 63 + rest_days * 127

diff = abs(norm_play_time - play_time)
hours = diff // 60
minutes = diff % 60

if norm_play_time > play_time:
    print(f'Tom sleeps well\n{hours} hours and {minutes} minutes less for play')
else:
    print(f'Tom will run away\n{hours} hours and {minutes} minutes more for play')
