import re

regex = r"(\b\d{2}([\.\-/])[A-Z][a-z]{2}\2\d{4})"
dates = re.findall(regex, input())

for element in [date for date, sep in dates]:
    day = element[:2]
    month = element[3:6]
    year = element[7:]
    print(f'Day: {day}, Month: {month}, Year: {year}')
