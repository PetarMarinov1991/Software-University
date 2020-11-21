from math import ceil

frames_time = int(input())
scenes = int(input())
scene_duration = int(input())

preparation = frames_time * 0.15
filming_duration = scenes * scene_duration
total_time = preparation + filming_duration

diff = ceil(abs(total_time - frames_time))

if frames_time >= total_time:
    print(f'You managed to finish the movie on time! You have {diff} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {diff} minutes.')
