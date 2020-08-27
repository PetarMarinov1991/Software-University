import re

regex = r"([=|/])([A-Z][A-Za-z]{2,})\1"

data = re.findall(regex, input())

destinations = []
travel_points = 0
for match in data:
    destinations.append(match[1])
    travel_points += len(match[1])

print(f'Destinations: {", ".join([x for x in destinations])}')
print(f'Travel Points: {travel_points}')
