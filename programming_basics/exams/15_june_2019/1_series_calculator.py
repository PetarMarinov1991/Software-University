import math

series_title = input()
seasons = int(input())
episodes = int(input())
episode_time = int(input())

commercial_time = 0.2 * episode_time
total_episode_time = episode_time + commercial_time
season_end_time = seasons * 10
total_series_time = episodes * total_episode_time * seasons + season_end_time

print(f'Total time needed to watch the {series_title} series is {math.floor(total_series_time)} minutes.')
