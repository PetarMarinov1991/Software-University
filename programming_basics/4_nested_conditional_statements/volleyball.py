import math

year_type = input()
holidays_count = int(input())
weekends_home = int(input())

weekends = 48
weekends_in_sofia = weekends - weekends_home
games_played = (3/4 * weekends_in_sofia) + weekends_home + (2/3 * holidays_count)

if year_type == 'leap':
    games_played *= 1.15

print(math.floor(games_played))
